Questions=[
["Who is the first Asian American to feature on US currency?", "Anna May Wong","Elizabeth Sung","Jadin Wong","Vera Wong",1],
["The Amazon Fund is maintained by which financial institution?", "World Bank","IMF","New Development Bank","Brazilian Development Bank",4],
["“Gateway to the Underworld” is an artefact belonging to which country?" ,"India","Sri Lanka","Mexico","USA",3],
["Grasslands found in Africa are called?","Prairies","Steppes","Savannah","Pampass",3],
["What is the underwater mountain system formed by plate tactonic spreading called?", "Mid oceanic Ridge","Oceanic Trench","Continental Slope","Abyssal Plains",1],
["Which is the southernmost active volcano on earth?", "Mount Dukono","Mount Rainier","Mount Semeru","Mount Erebus",4],
["Which forests act as barriers against cyclones?" ,"Alpine forests","Mangrove forests","Evergreen forests","Monsoon forests",2],
["Which country is the largest producer of desalinated sea water?","Kuwait","Iran","Saudi Arabia","Iraq",3],
["Continent which has no active volcanic regions is ?","North America","Europe","Australia","Africa",3],
["Autobiography “Daughter of Destiny” is written by?","Benazir Bhutto" ,"Mumtaz Bhutto","Waheed Rehman","Aslam Memon",1],
    ]
levels=[1000,3000,5000,7000,10000,50000,100000,200000,300000,500000]
money=0
for i in range(0,len(Questions)):
    question=Questions[i]
    print(f"\n\nQuestion, for Rs. {levels[i]} " )
    print(question[0])
    print(f"a.{question[1]}         b.{question[2]}")
    print(f"c.{question[3]}         d.{question[4]}")
    reply=int(input("enter yor answern or 0 to quit"))
    if (reply==0):
        money=levels[i]
        break
    if (reply==question[-1]):
        print(f"correct answer \ncongratulation! you won Rs{levels[i]}")
        if(i==4):
            money = 10000
        elif(i==9):
            money=500000
    else:
        print(f"wrong answer!")
        break
print(f"your take home money is {money} ")