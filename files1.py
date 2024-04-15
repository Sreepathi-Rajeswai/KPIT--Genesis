#i. count number of words
fin=open("C://Users/SREEPATHIR/Documents/lava/data.txt","r")
fout=open("C://Users/SREEPATHIR/Documents/lava/output1.txt","a+")
s=0
for i in fin:
   k=i.split()
   s+=len(k)
print("count individual word",s)
#ii. and iii. no. of occurences and print in a new file
'''fin=open("C://Users/SREEPATHIR/Documents/lava/data.txt","r")
fout=open("C://Users/SREEPATHIR/Documents/lava/output1.txt","a+")
l={}
for i in fin:
   h=i.split()
   for j in h:
      if j not in l:
         l[j]=1
      else:l[j]+=1
   for w,c in l.items():
      print(fout.write("%s\t%d\n"%(w,c)))'''





    