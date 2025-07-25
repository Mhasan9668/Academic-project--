x=6 
if x>10:
    print("it is true")
else:
    print("it is false")
print("end")

x=int(input("pleas enter a number"))
if x % 2 == 1:
    print(f"{x} the number is even")
else :
    print(f"{x} the number is odd")

x= int(input("please enter marks "))
if x>=80:
    print("grade A+")
    age= int(input("please enter your age"))
    if age < 20:
        print("you are teenager you have a time to increas you persentage")
    else :
        print("now it time to work hard in you practical life")
elif x>=70:
    print("grade A")
    age= int(input("please enter your age"))
    if age < 20:
        print("you are teenager you have a time to increas you persentage")
    else :
        print("now it time to work hard in you practical life")
elif x>= 60:
    print("grade B")
    age= int(input("please enter your age"))
    if age < 20:
        print("you are teenager you have a time to increas you persentage")
    else :
        print("now it time to work hard in you practical life")
elif x>=50:
    print ("grade C")
    age= int(input("please enter your age"))
    if age < 20:
        print("you are teenager you have a time to increas you persentage")
    else :
        print("now it time to work hard in you practical life")
else:
    print("fail")
    print("you have to need attention")

print("exit")

s1="python programming"
l=len(s1)
x=0
while x<l:
    if s1[x] not in "aeiou":
         print(s1[x])
    x=x+1

sum =0
x=''
while x != "n":
    x=input("please enter a number")
    if x!= 'n':
        sum =sum + int(x)
print (sum)

#i=1

while i<=5:
    j=1
    while j<=i:
        j=j+1
        print(j, end = ' ')
    print()
    i=i+1
s1 = "python programing language"
for x in s1:
    print(x)
for y in range(1,11):
    print(y)
for z in range (1,11,2):
    print(z)
for x in s1:
    if x not in "aeiou":
        print(x)
    else :
        print ("exit")
for i in range(1,6):
    for j in range(1,i+1):
        print(j ,end=' ')
    print("end")
i=1
while i<=5:
    if i==3 :
        i=i+1
        continue
    print(i)
    i=i+1
s1="hello world"
for x in s1:
    if x in "aeiou":
        continue
    print(x)
i=1
while i<=5:
    if i==3 :
        i=i+1
        break
    print(i)
    i=i+1
s1="hello world"
for x in s1:
    if x in "aeiou":
        break
    print(x)
fruit_name= ["apple", "mango,","banana","orange", "cherry"]
print(fruit_name)
print(type(fruit_name))
print(fruit_name[3])
print(fruit_name[1:3])
fruit_name[4] = "grapes"
fruit_name.append("cherry")
fruit_name.insert(4,"pineapple")
fruit_name.remove("apple")
print(fruit_name)

marks=[120,200,150,180,220,300]
l=len(marks)
i=0
while i<l:
    print(marks[i])
    i=i+1
max=marks[0]
for m in marks:
    if m>max:
        max=m
print(m)
#even=[]
number=[10,20,47,28,33,89,100,88,27,]
for n in number:
    if n %2==0:
        even.append(n)
print(even)
even=[n for n in number if n%2==0 ]
print (even)
