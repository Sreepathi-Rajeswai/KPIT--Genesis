'''l="JKLMNOPQ"
s='ack'
for k in l:
    m=(l[-3]) 
    h=(l[-1])
    if m in k:print(k+"uack")
    elif h in k:print(k+"uack")
    else:print(k+s)'''
#print vowels in a string
'''def vowels(n):
    d=input().split(",")
    c=0
    for i in n:
        for j in d:
            if i == j:
                c=c+1
    return c
n=input().lower()
print(vowels(n))'''
#print words more than five charecters in a list
#list=["kavya","padma","rajeswari","pravalika","riddhi","sruthi","sejalchowdary"]
'''def fun(list):
    l=[]
    for i in list:
        if len(i)>5:l.append(i)
    return l
list=list(map(str,input().split(",")))
print(fun(list))'''
#3
'''t=tuple(map(int,input().split(",")))
s=0
for i in t:
    s=s+i
    a=s/len(t)
print(a)
print(s)'''
#4
'''def dict(a):
    s=0
    for i in a.values():
        s=s+i
        p=s/len(a)
    return p
a={"maths":50, "telugu":80 ,"hindi":70, "physics":80, "social":80 ,"english":80}
print(dict(a))'''
#5
'''fin=open("Documents/example_data.csv","r")
fout=open("C://Users/SREEPATHIR/Documents/lava/output.txt","+a")
for i in fin:
    h=i.split(",")
    if h[1]>str("30"):
        m=h[0]
        print(m)        
        print(fout.write(m+"\n"))'''
#6
'''fin=open("C://Users/SREEPATHIR/Documents/lava/data.txt","r")
fout=open("C://Users/SREEPATHIR/Documents/lava/sana.txt","a+")
l={}
for i in fin:
   h=i.split()
   for j in h:
      if j not in l:
         l[j]=1
      else:l[j]+=1
for w,c in l.items():
    print(fout.write("%s\t%d\n"%(w,c)))'''
'''a=[1,2,3,4,5,6,7,8,9]

a[::2]=10,20,30,40,50,60
print(a)'''
'''a=[1,2,3,4,5,6,7,8,9]
print(a[::2])'''
'''rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}

id1 = id(rec)

del rec

rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}

id2 = id(rec)

print(id2==id2)'''
'''a=4
b=11
print(a|b)
print(a>>2)
print(-18//4)'''
'''y=10
x=y+=2
print(y)'''
m=[1,2,3,4,5,6]
for i in m:
    m.remove(i)
print(m)


    

    