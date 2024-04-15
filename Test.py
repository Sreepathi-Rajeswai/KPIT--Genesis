#print("Hello World")
# second program
#print(72**17)
#print (2++2)
#print(0111)
#print(2 2)
#print(42*60+42)
#print(10*1.61)
#average speed of the distance
'''a=10*1.61#convert kilometers into miles
b=(42*60+42)/3600# convert minutes into hour
c=a/b #average speed of disatnce
print(c)'''
'''x=4;y=5
print(x*y)
print(4/3*3.14*5**3)'''
#646
'''a=24.95*0.4#$24.95 cost and 40% discount
b=a*60
c=3+0.75*59+b
print(c)'''
#3.if i leave my house at 6:52 am and run 1 mile at an easy pace(8:15 per mile),than 3 miles at tempo(7:12 per mile) and 1 mile at easy,what time i go for breakfast
#(pending)
'''a=(6*60+52)*60
b=(8*60+15)*2
c=(7*60+12)*3
time=(a+b+c)//60*60
t1=time%60
print(time+t1)'''
'''import math
p=math.sqrt(2)
print(p)'''

'''from datetime import datetime,time,timedelta
time1=datetime.combine(date.today(),time(6,52,00))
#start=(6*60+52)*60
ease=2*timedelta(8,15)
tempo=3*timedelta(7,12)
print(time1+ease+tempo)'''
'''b =2*time(0,34,45)
print(b)'''


#4
'''def print_lyrics():
    print("lm ok")
    print("i work well")
def rev_lyrics():
    print_lyrics=()
    print_lyrics=()
print(rev_lyrics())'''
#5 (pending)
'''def right_justify(s):
    s=input("")
    l=s.len()
    print(l)'''
#6(pending)
'''r=int(input())
c=int(input())
for i in range(1,r+1):
    i+=1
    print(1*1,6*6,11*11,end="+")
    for j in range(1,c+1):'''
#7(pending)
'''name="what is your name"
s=int(input(name))
l=int(s)'''
#8 a^n+b^n=c^n
'''import math
a,b,c=map(int,input().split())
n=int(input())
d=math.pow(a,n)
f=math.pow(b,n)
h=math.pow(c,n)
if d+f==h:
    print("True")
else:print("False")'''
#9 factorial
'''n=int(input())
f=1
if n==0 and n==1:
    print("1")
else:
    for i in range(1,n+1):
        f=f*i
    print(f)'''

#10 reverse
'''n=input("")
s=n[::-1]
if n==s:print("True")
else:print("False")'''
#11pending
'''import math
def mysqrt(a):
    while True:
        x=y=1
        print(x)
        y=(x+a/x)/2
        if y==x:
            break
x=y'''
#12
'''import math
n=input()
while n!='done':
    a=eval('math.sqrt(5)')
    b=eval('type(math.pi)')
    print(a,b)'''
#13(homework)
#14 test
'''s="oack"
for i in s:
    print(i)
    if i[0]=="o" or "q":
        i=="u"
        print(i)'''
#15
'''w='banana'
c=0
for i in w:
    if i=='a':
        c=c+1
        print(c)'''
#16
'''def af(s):
    for c in s:
        if not c.islower():return False
    return True
s=input("")
print(af(s))'''
#17 check
'''fin=open('C:/Users/SREEPATHIR/Documents/lava')
for i in fin:
    print(i)
    i=i+1
    if i>=8:break
print(fin)'''
#18
'''t=['d','e','f']
t.sort()
print(t)'''
#19
'''s=[1,2,3]
if s.sort():
    print("True")
else:print("False")'''
#20 CHECK
'''import numpy
words=["banana","apple","kiwi","orange"]
s=input("")
for i in words (numpy(s)):
        print(i)'''
#21
'''def invert_dict(d):
  inverse = {}
  for key in d:
    new_key = d[key]
    inverse.setdefault(new_key, [])
  return inverse

letters_in_word = {"mine": 4, "yours": 5, "ours": 4, "sunday": 6, "friend": 6, "fun": 3, "happy": 5, "beautiful": 8}

print (invert_dict(letters_in_word))'''
#22
'''def sum_all(*args):
    s=0
    for i in args:
        s=s+i
    return s
print(sum_all(1,2,3,4));'''
#23
'''fin=open("C://Users/SREEPATHIR/Documents/lava/sana.txt")
print(fin)
for line in fin:
    line.split()
    p=list(line)
    p.sort()
    print(p)'''
#24
'''def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")
def repeat_lyrics():
    print_lyrics()
    print_lyrics()
print_lyrics()'''
#25
'''p='im here'
s=input(p)
print(int(s))'''
#26
'''import math
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result
x1,x2,y1,y2=map(int,input().split())
print(distance(x1,x2,y1,y2))'''
#27
'''from collections import Counter, defaultdict

def anagram(words):
    anagrams = defaultdict()
    for word in words:
        histogram =[] # build a hashable histogram
        anagrams[histogram].append(word)
    return (anagrams.values())

keywords = open("C://Users/SREEPATHIR/Documents/lava/sana.txt")
p=keywords.read().split()'''
'''s="apple"
_s1="tom"
print(_s1*2)'''


'''print(anagram(p))'''
#28
'''def do_twice(print_spam):
    print_spam()
def print_spam():
    print('spam')
    print('spam')
print_spam(do_twice)'''
#29
'''import datetime
epic=datetime.datetime(1970,1,1)
p=datetime.datetime.now()
print(p-epic)'''
#30
'''def lower(s):
    for c in s:=
        if c.islower():
            return 'True'
        else:return 'False'
s='banana'
print(lower(s))'''
#31
'''def right(s):
    l=" "*65
    return l+s
s='montify'
print(right(s))'''
#32 grid
'''def grid():
    print("+",4*"-",'+',4*'-','+',4*'-','+')
def grid1():
    for x in range(4):
        print('|',4*' ','|',4*' ','|',4*' ','|')
def total(n):
    grid()
    grid1()
    grid()
    grid1()
    grid()
    grid1()
    grid()
    return ""
print(total(5))'''
#33
#s=int(input())
#hcf
'''def compute_hcf(x, y):
   while(y):
       print(y)
       x, y = y, x % y
       print(x,y)
   return x

hcf = compute_hcf(300, 400)
print("The HCF is", hcf)'''
#gcd
'''s="this \110\145"
print(s)'''
#interchange first to last element
'''l=[1,2,3,4,56,9]
a = l[0]
b = l[-1]
a, b=b, a
l[0] = a
l[-1] = b
print(l)'''
#smallest number in a list same for largest
'''l=[1,9,3,5,34,34,4]
l.sort()
print(l,"\nsmallest:",l[0] )
l.remove(l[0])
print("2nd smallest:",l[0])'''
#string of first and last letter become upper
'''s = "welcome to geeksforgeeks"
a = s.split()
res = []
for i in a:
    x = i[0].upper()+i[1:-1]+i[-1].upper()
    res.append(x)
res = " ".join(res)
print("String after:", res)'''
#accept only if they are vowels
'''import collections

def check(string):
	# create a Counter object to count the occurrences of each character
	counter = collections.Counter(string.lower())
	
	# set of vowels
	vowels = set("aeiou")
	
	# counter for the number of vowels present
	vowel_count = 0
	
	# check if each vowel is present in the string
	for vowel in vowels:
		if counter[vowel] > 0:
			vowel_count += 1
	
	# check if all vowels are present
	if vowel_count == len(vowels):
		print("Accepted")
	else:
		print("Not Accepted")

# test the function
string = "SEEquoiaL"
check(string)'''
#reverse a word in a string
'''s=input().split()
for i in s:
    print(i[::-1], end=" ")'''
#factorial
'''# Python code to demonstrate naive method
# to compute factorial
n = 23
fact = 1

for i in range(1, n+1):
	fact = fact * i

print("The factorial of 23 is : ", end="")
print(fact)
#fibinocci
n = 10
num1 = 0
num2 = 1
next_number = num2 
count = 1

while count <= n:
	print(next_number, end=" ")
	count += 1
	num1, num2 = num2, next_number
	next_number = num1 + num2
print()'''
#fib
'''def fibinoci(n):
    if n>0:
        print(1)
    return fibinoci(n-1)+fibinoci(n-2)
print(fibinoci(9))'''
#
'''def Fibonacci(n):

	# Check if input is 0 then it will
	# print incorrect input
	#if n < 0:
		#print("Incorrect input")

	# Check if n is 0
	# then it will return 0
	#elif n == 0:
		#return 0

	# Check if n is 1,2
	# it will return 1
	#elif n == 1 or n == 2:
		#return 1

	#else:
	return Fibonacci(n-1) + Fibonacci(n-2)


# Driver Program
print(Fibonacci(9))'''

import math
import re
h=float(input())
l=float(input())
a=float(input())
a1=math.radians(a)
s1=2*h
s2=1
a2=0.5*s1*s2*a1
a3=0.5*l*l*math.sin(a1)
t=a2-a3
m=re.search(r'\d+\.\d+',t)
k=float(m.group())
print(round(m,3))



    




    



    



    

        







