st=input("enter the massege")
words=st.split(" ")
coding=input("1 for coding or 0 for decoding")
coding= True if(coding=="1") else False
print(coding)
if (coding):
    nwords=[]
    for word in words:
        if (len(word)>=3):
            a1=input("enter rendum")
            a2=input("enter rendum")
            stnew=a1+word[1:]+word[0]+a2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" " .join(nwords))
else:
    nwords=[]
    for word in words:
        if (len(word)>=3):
            stnew=word[3:-3]
            stnew=stnew[-1]+stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" " .join(nwords))