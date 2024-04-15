'''def invert_dict(d):
  inverse = {}
  for key in d:
    val = d[key]
    inverse.setdefault(key,1)
  return inverse
word = {"a": 4, "b": 5, "c": 4, "d": 6, "e": 6,}
print (invert_dict(word))'''
#13.3
'''import string
def process_file(fin):
    fin=open("C://Users/SREEPATHIR/Documents/lava/sana.txt")
    hist=dict()
    for line in fin:
        process_file(line,hist)
    return hist
def process_line(line,hist):
    line=line.replace("-"," ")
    for w in line.split():
        w=w.strip(string.punctuation+string.whitespace)'''
#
'''def random(h):
    h={"top":1,"pot":2,"the":3}
    t=[]
    for w,f in h.items():
        t.extend([w]*f)
    return t
h={"top":1,"pot":2,"the":3}
print(random(h))'''
#14.3
'''x=42
'%d' % x
print(x)'''
#14.4
'''import os
cwd=os.getcwd()
#os.path.abspath("sana.txt")
#os.listdir(cwd)
def wall(dirname):
      for n in os.listdir(dirname):
        p=os.path.join(dirname,n)
        if os.path.isfile(p):
            print(p)
        else:wall(p)
wall(cwd)'''

#os.listsir(cwd)
#excercise 14.1
'''def sed(s,rs,p,k):
    p=open("C://Users/SREEPATHIR/Documents/lava/sana.txt",'r')
    #k=open("C://Users/SREEPATHIR/Documents/lava/Fil.txt",'w')
    for l in p:
       m=l.split()
    k=open("C://Users/SREEPATHIR/Documents/lava/Fil.txt")
    for t in k:
       j=t.split()
    if s==(p) and k:
          s.replace(s,rs)
    return m
s="in"
rs="im"
p=open("C://Users/SREEPATHIR/Documents/lava/sana.txt",'r')
k=open("C://Users/SREEPATHIR/Documents/lava/Fil.txt",'w')
print(sed(s,rs,p,k))'''
#excersise 14.3
'''def all(dirf):
    import os
    m=[]
    for x,z in dirf:
        print(x,z)
        if len(z)>0:
            for i in z:
                if i[-1]=='3':
                    m.append(x+'/'+i)
    return m
dirf=open("C://Users/SREEPATHIR/Documents/lava/Fil.txt")
print(all(dirf))'''
#distance between two arguments
'''import math
class point:
   def __main__(x,y):
       x=3;y=4
def distance(x,y):
    d=math.sqrt((blank.x1-blank.x)**2+(blank.y1-blank.y)**2)
    return d
blank=point()
x=3;y=4
blank.x=3;blank.x1=7;blank.y=4;blank.y1=8
print(distance(x,y))
#add method
class add:
    def __main__(self,x,y):
        self.x=x;self.y=y
    def point(x,y):
        d=x+y
        return d
x=3;y=4
x.point()'''
#sort dictionary by using keys or values
'''d={"mom":90,"dad":70,"sis":39423,"bestie":89}
for i in sorted(d.items()):
    print(i,end=" ")'''
#for dictionary sum of keys you need to convert into list and then perform sum()
#lenght of dict
'''d={"mom":90,"dad":70,"sis":39423,"bestie":89}
k=len(d),str(d.__sizeof__())
print(k)'''
#sort using lamda
'''list = [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]
 
# using sorted and lambda to print list sorted
# by age
print("The list printed sorting by age: ")
print(sorted(list, key=lambda i: i['age']))
 
print("\r")
 
# using sorted and lambda to print list sorted
# by both age and name. Notice that "Manjeet"
# now comes before "Nandini"
print("The list printed sorting by age and name: ")
print(sorted(list, key=lambda i: (i['age'], i['name'])))
 
print("\r")
 
# using sorted and lambda to print list sorted
# by age in descending order
print("The list printed sorting by age in descending order: ")
print(sorted(list, key=lambda i: i['age'], reverse=True))'''
#merge two dic using update
'''d={"mom":90,"dad":90}
d1={"bestie":80,"sis":90}
d1.update(d)
print(d1)'''
#common elements in two arrays
'''def common_elements(ar1, ar2, ar3):
    n1, n2, n3 = len(ar1), len(ar2), len(ar3)
    i, j, k = 0, 0, 0
    common = []
    while i < n1 and j < n2 and k < n3:
        if ar1[i] == ar2[j] == ar3[k]:
            common.append(ar1[i])
            i += 1
            j += 1
            k += 1
        elif ar1[i] < ar2[j]:
            i += 1
        elif ar2[j] < ar3[k]:
            j += 1
        else:
            k += 1
    return common
     
ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
print(common_elements(ar1, ar2, ar3)) # Output: [20, 80]
 
ar1 = [1, 5, 5]
ar2 = [3, 4, 5, 5, 10]
ar3 = [5, 5, 10, 20]
print(common_elements(ar1, ar2, ar3)) # Output: [5, 5]'''
#max votes
'''from collections import Counter 
 
def winner(input): 
 
    # convert list of candidates into dictionary 
    # output will be likes candidates = {'A':2, 'B':4} 
    votes = Counter(input) 
     
    # create another dictionary and it's key will 
    # be count of votes values will be name of 
    # candidates 
    dict = {} 
 
    for value in votes.values(): 
 
        # initialize empty list to each key to 
        # insert candidate names having same 
        # number of votes 
        dict[value] = [] 
 
    for (key,value) in votes.items(): 
        dict[value].append(key) 
 
    # sort keys in descending order to get maximum 
    # value of votes 
    maxVote = sorted(dict.keys(),reverse=True)[0] 
 
    # check if more than 1 candidates have same 
    # number of votes. If yes, then sort the list 
    # first and print first element 
    if len(dict[maxVote])>1: 
        print (sorted(dict[maxVote])[0])
    else: 
        print (dict[maxVote][0]) 
 
# Driver program 
if __name__ == "__main__": 
    input =['john','johnny','jackie','johnny',
            'john','jackie','jamie','jamie',
            'john','johnny','jamie','johnny',
            'john'] 
    winner(input)'''
#max values with key
'''d={"Gfg" : [5, 7, 9, 4, 0], "is" : [6, 7, 4, 3, 3], "Best" : [9, 9, 6, 5, 5]}
for k,v in d.items():
    #unique_counts = [(key, len(set(values))) for key, values in test_dict.items()]
    l=set(v)
    print(l,k)'''
'''test_dict = {"Gfg": [5, 7, 5, 4, 5],
             "is": [6, 7, 4, 3, 3],
             "Best": [9, 9, 6, 5, 5]}
 
# Printing the original dictionary
print("The original dictionary is : " + str(test_dict))
 
# Creating a list of tuples
# where each tuple contains the key and
# the number of unique values
# using list comprehension
unique_counts = [(key, len(set(values))) for key, values in test_dict.items()]
#print(un)
 
# Finding the key with the maximum unique values
# using the max() function with a key argument
max_key = max(unique_counts, key=lambda x: x[1])[0]

 
# Printing the result
print("Key with maximum unique values : " + str(max_key))'''
#duplicate charecters in dict
'''def duplicate_characters(string):
    # Create an empty dictionary
    chars = {}
 
    # Iterate through each character in the string
    for char in string:
        # If the character is not in the dictionary, add it
        if char not in chars:
            chars[char] = 1
        else:
            # If the character is already in the dictionary, increment the count
            chars[char] += 1
 
    # Create a list to store the duplicate characters
    duplicates = []
 
    # Iterate through the dictionary to find characters with count greater than 1
    for char, count in chars.items():
        if count > 1:
            duplicates.append(char)
 
    return duplicates
 
# Test cases
print(duplicate_characters("geeksforgeeks"))'''
#similar group items in one key
'''test_list = [4, 6, 6, 4, 2, 2, 4, 4, 8, 5, 8]
 
# printing original list
print("The original list : " + str(test_list))
 
# using set() to get unique elements in list
unique_items = set(test_list)
 
# creating dictionary with empty lists as values
res = {key: [] for key in unique_items}
 
# using list comprehension to group similar items
[res[item].append(item) for item in test_list]
 
# printing result
print("Similar grouped dictionary : " + str(res))'''
#assign dict
'''test_list = ["Gfg", "is", "Best"]
 
# printing original list
print("The original list : " + str(test_list))
 
# initializing subs. Dictionary
subs_dict = {
    "Gfg" : [5, 6, 7], 
    "is" : [7, 4, 2], 
}
 
# initializing K 
K = 2
 
# using list comprehension to solve
# problem using one liner
res = [ele if ele not in subs_dict else subs_dict[ele][K]
                                     for ele in test_list]
print("The list after substitution : " + str(res))'''
#del key from dict
'''d={"mom":90,"dad":90,"sis":89,"bestie":89}
del d["bestie"]
print(d)'''
#replace string into dict
'''test_str = 'geekforgeeks best for geeks'
 
# printing original string
print("The original string is : " + str(test_str))
 
# lookup Dictionary
lookp_dict = {"best" : "good and better", "geeks" : "all CS aspirants"}
 
# performing split()
temp = test_str.split()
res = []
for wrd in temp:
     
    # searching from lookp_dict
    res.append(lookp_dict.get(wrd, wrd))
     
res = ' '.join(res)
 
# printing result 
print("Replaced Strings : " + str(res))'''
#remove keys
'''test_str = 'gfg is best for geeks'
 
# printing original string
print("The original string is : " + str(test_str))
 
# initializing Dictionary
test_dict = {'geeks': 1, 'best': 6}
 
# Remove Dictionary Key Words
# Using split() + loop + replace()
for key in test_dict:
    if key in test_str.split(' '):
        test_str = test_str.replace(key, "")
 
# Printing result
print("The string after replace : " + str(test_str))'''
#remove duplicates
'''s = "Python is great and Java is also great"
l = s.split()
k = []
for i in l:
 
    # If condition is used to store unique string 
    # in another list 'k' 
    if (s.count(i)>=1 and (i not in k)):
        k.append(i)
print(' '.join(k))'''
#remove duplicate values
# Python3 code to demonstrate working of
# Remove duplicate values across Dictionary Values

# initializing dictionary
'''test_dict = {'Manjeet': [1, 4, 5, 6],
			'Akash': [1, 8, 9],
			'Nikhil': [10, 22, 4],
			'Akshat': [5, 11, 22]}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Remove duplicate values across Dictionary Values
x = []
for i in test_dict.keys():
	x.extend(test_dict[i])
y = []
for i in x:
	if(x.count(i) == 1):
		y.append(i)
res = dict()

for i in test_dict.keys():
	a = []
	for j in test_dict[i]:
		if j in y:
			a.append(j)
		res[i] = a

# printing result
print("Uncommon elements records : " + str(res))'''
#counting frequencies in a list using dict
'''def CountFrequency(my_list):
 
    # Creating an empty dictionary
    count = {}
    for i in [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]:
        count[i] = count.get(i, 0) + 1
    return count
 
 
# Driver function
if __name__ == "__main__":
    my_list = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
    print(CountFrequency(my_list))'''
#dict value mean
'''test_dict = {"Gfg" : 4, "is" : 7, "Best" : 8, "for" : 6, "Geeks" : 10} 
  
# printing original dictionary 
print("The original dictionary is : " + str(test_dict)) 
  
# loop to sum all values  
res = 0
for val in test_dict.values(): 
    res += val 
  
# using len() to get total keys for mean computation 
res = res / len(test_dict) 
  
# printing result  
print("The computed mean : " + str(res)) '''
#mirror charecters
'''def mirrorChars(input,k):
 
    # create dictionary
    original = 'abcdefghijklmnopqrstuvwxyz'
    reverse = 'zyxwvutsrqponmlkjihgfedcba'
    dictChars = dict(zip(original,reverse))
 
    # separate out string after length k to change
    # characters in mirror
    prefix = input[0:k-1]
    suffix = input[k-1:]
    mirror = ''
 
    # change into mirror
    for i in range(0,len(suffix)):
         mirror = mirror + dictChars[suffix[i]]
 
    # concat prefix and mirrored part
    print (prefix+mirror)
          
# Driver program
if __name__ == "__main__":
    input = 'paradox'
    k = 3
    mirrorChars(input,k)'''
#extract unique dict values
'''test_dict = {'gfg': [5, 6, 7, 8],
             'is': [10, 11, 7, 5],
             'best': [6, 12, 10, 8],
             'for': [1, 2, 5]}
 
# printing original dictionary
print("The original dictionary is : " + str(test_dict))
 
# Extract Unique values dictionary values
# Using set comprehension + values() + sorted()
res = list(sorted({ele for val in test_dict.values() for ele in val}))
 
# printing result
print("The unique values list is : " + str(res))'''
#check the posiibilities of the dict
'''# Function to print words which can be created
# using given set of characters



def charCount(word):
	dict = {}
	for i in word:
		dict[i] = dict.get(i, 0) + 1
	return dict


def possible_words(lwords, charSet):
	for word in lwords:
		flag = 1
		chars = charCount(word)
		for key in chars:
			if key not in charSet:
				flag = 0
			else:
				if charSet.count(key) != chars[key]:
					flag = 0
		if flag == 1:
			print(word)

if __name__ == "__main__":
	input = ['goo', 'bat', 'me', 'eat', 'goal', 'boy', 'run']
	charSet = ['e', 'o', 'b', 'a', 'm', 'g', 'l']
	possible_words(input, charSet)'''
#maximum record key value in dict
'''# Python3 code to demonstrate working of 
# Maximum record value key in dictionary
# Using loop

# initializing dictionary
test_dict = {'gfg' : {'Manjeet' : 5, 'Himani' : 10},
			'is' : {'Manjeet' : 8, 'Himani' : 9},
			'best' : {'Manjeet' : 10, 'Himani' : 15}}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing search key
key = 'Himani'

# Maximum record value key in dictionary
# Using loop
res = None
res_max = 0
for sub in test_dict:
	if test_dict[sub][key] > res_max:
		res_max = test_dict[sub][key]
		res = sub

# printing result 
print("The required key is : " + str(res))'''
#extract values of particular key
'''# Python3 code to demonstrate working of 
# Extract values of Particular Key in Nested Values
# Using list comprehension

# initializing dictionary
test_dict = {'Gfg' : {"a" : 7, "b" : 9, "c" : 12},
			'is' : {"a" : 15, "b" : 19, "c" : 20}, 
			'best' :{"a" : 5, "b" : 10, "c" : 2}}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing key
temp = "c"

# using item() to extract key value pair as whole
res = [val[temp] for key, val in test_dict.items() if temp in val]

# printing result 
print("The extracted values : " + str(res))''' 



