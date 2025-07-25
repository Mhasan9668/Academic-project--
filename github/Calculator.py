
n=int(input("enter the number"))
operator=input("enter the operator")
m=int(input("enter the number"))
print(n,operator,m)
if(operator=="+"):
  print (n + m) 
elif(operator=="-"):
  print(n-m)
elif(operator=="*"):
  print(n*m)
elif(operator=="/"):
  print(n/m)
elif(operator=="%"):
  print(n%m)
elif(operator=="**"):
  print(n**m)
elif(operator=="//"):
  print(n//m)
else:
  print("invaled operator")
print("thank you")
