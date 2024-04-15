#1 write a python program that takes a paragraph as input and ouput for upper,reverse code,reverse charecters,number of charecters
s=input().lower()
c=0
#S=0
for i in s:
    c+=1
print("print number of charecters",c)#i
print("paragraph in upper case",s.upper())#ii.
for j in s.split(" "):
    #S+=1
    print(j[::-1],end=" ")#v
    #l=len(j)
#print(len(j)//S)
l=[]#iii.
k=s.split()[::-1]
for i in k:
    l.append(i)
print("\nparagraph in reverse:"," ".join(l))

#print average lenght
s=input().split()#iv.
avg=sum(len(i) for i in s)/len(s)
print("avarage of word lenght",avg)

