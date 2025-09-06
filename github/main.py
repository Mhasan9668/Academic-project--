from dotenv import load_dotenv
import os
import chainlit as cl
import time
import pandas as pd
import matplotlib.pyplot as plt
from typing import List, Dict, Any
from pydantic import Field
import pandas as pd
import numpy as np
from agents import (
    Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel,
    set_tracing_disabled, set_default_openai_client,
    function_tool
)

# Load env
_ = load_dotenv()

# Disable tracing
set_tracing_disabled(disabled=True)

# 1. Connect LLM service
external_client: AsyncOpenAI = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# 2. Model
llm_model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client
)
set_default_openai_client(external_client)

# ---------------- BI TOOLS ---------------- #
@function_tool
def load_data_tool(file_path: str) -> str:
    """Loads CSV/XLSX file into a dataframe and returns preview."""
    ext = file_path.split(".")[-1].lower()
    if ext == "csv":
        df = pd.read_csv(file_path)
    elif ext in ["xlsx", "xls"]:
        df = pd.read_excel(file_path)
    else:
        return "Unsupported file format"
    return df.head().to_markdown()


@function_tool
def clean_data_tool(df_json: str) -> str:
    """Clean dataframe: fill missing values, drop duplicates, etc."""
    df = pd.read_json(df_json, orient="split")
    df = df.fillna(0).drop_duplicates()
    return df.to_json(orient="split")

@function_tool
def analyze_data_tool(df_json: str, operation: str, column: str) -> str:
    """Perform analysis: mean, median, mode, std, sum, etc."""
    import numpy as np
    from statistics import mode

    df = pd.read_json(df_json, orient="split")
    series = df[column]

    if operation == "mean":
        result = series.mean()
    elif operation == "median":
        result = series.median()
    elif operation == "mode":
        try:
            result = mode(series)
        except:
            result = series.mode().iloc[0]
    elif operation == "std":
        result = series.std()
    elif operation == "sum":
        result = series.sum()
    elif operation == "count":
        result = series.count()
    else:
        result = f"Operation {operation} not supported"

    return f"{operation} of {column} = {result}"

@function_tool
def visualize_data_tool(df_json: str, chart_type: str, x: str, y: str, output_file="chart.png") -> str:
    """Generate visualization: bar, line, donut, etc."""
    df = pd.read_json(df_json, orient="split")
    plt.figure(figsize=(6,4))

    if chart_type == "bar":
        df.groupby(x)[y].sum().plot(kind="bar")
    elif chart_type == "line":
        df.groupby(x)[y].sum().plot(kind="line")
    elif chart_type == "donut":
        df.groupby(x)[y].sum().plot(kind="pie", autopct='%1.1f%%')
        plt.gca().set_ylabel("")
    else:
        return "Chart type not supported"

    plt.title(f"{chart_type} chart of {y} by {x}")
    plt.savefig(output_file)
    return f"Chart saved to {output_file}"

# ---------------- Specialist Agents ---------------- #
data_cleaning_agent = Agent(
    name="Data Cleaning Agent",
    handoff_description="Specialist agent for cleaning data",
    instructions="You clean datasets by handling missing values, duplicates, and formatting.",
    tools=[clean_data_tool],
    model=llm_model
)

data_analysis_agent = Agent(
    name="Data Analysis Agent",
    handoff_description="Specialist agent for statistical analysis",
    instructions="You perform statistical analysis: mean, median, mode, sum, std, count, etc.",
    tools=[analyze_data_tool],
    model=llm_model
)

data_visualization_agent = Agent(
    name="Data Visualization Agent",
    handoff_description="Specialist agent for creating visuals",
    instructions="You generate charts (bar, line, donut, KPI) from the dataset.",
    tools=[visualize_data_tool],
    model=llm_model
)

# ---------------- Triage Agent ---------------- #
triage_agent = Agent(
    name="BI Triage Agent",
    instructions=(
        "Decide if the request is about cleaning data, analyzing data, or creating visuals. "
        "Then hand off to the right agent."
    ),
    handoffs=[data_cleaning_agent, data_analysis_agent, data_visualization_agent],
    model=llm_model
)

# ---------------- Chainlit Integration ---------------- #
conversation_history: List[Dict[str, str]] = []

@cl.on_message
async def main(message: cl.Message):
    global conversation_history
    start_time = time.time()

    if len(conversation_history) == 0:
        run_result = Runner.run_sync(triage_agent, message.content)
        conversation_history = run_result.to_input_list()
    else:
        run_result = Runner.run_sync(triage_agent, conversation_history + [{'content': message.content, 'role': 'user'}])
        conversation_history = run_result.to_input_list()

    end_time = time.time()
    print(f"Execution Time: {end_time - start_time:.2f} sec")

    await cl.Message(
        content=run_result.final_output
    ).send()


@cl.on_chat_start
async def start():
    await cl.Message(content="👋 Welcome to **Data Analyst Agent**!").send()