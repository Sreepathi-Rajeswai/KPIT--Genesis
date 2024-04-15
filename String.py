#reverse words in string
'''s="i like code"
l=[]
k=s.split()[::-1]
for i in k:
    l.append(i)
print(" ".join(l))'''
#substring in string
'''s="i love code"
if "love" in s:print("yes")
else:print("no")'''
#words frequency in string
'''# Python3 code to demonstrate working of
# Words Frequency in String Shorthands
# Using dictionary comprehension + count() + split()

# Initializing string
test_str = 'Gfg is best . Geeks are good and Geeks like Gfg'

# Printing original string
print("The original string is : " + str(test_str))

# Words Frequency in String Shorthands
# Using dictionary comprehension + count() + split()
res = {key: test_str.count(key) for key in test_str.split()}

# Printing result
print("The words frequency : " + str(res))'''
#check if all vowels in string
'''def check(string):
	string = string.replace(' ', '')
	string = string.lower()
	vowel = [string.count('a'), string.count('e'), string.count(
		'i'), string.count('o'), string.count('u')]

	# If 0 is present int vowel count array
	if vowel.count(0) > 0:
		return('not accepted')
	else:
		return('accepted')


# Driver code
if __name__ == "__main__":

	string = "SEEquoiaL"

	print(check(string))'''
#no.of matching charecters
'''s="amnshd"
s1="aukmdhj"
c=0
for i in s:
    for j in s1:
        if i==j:
            c+=1
print(c)'''
#remove all duplicates
'''def removeDuplicate(str): 
	s=set(str) 
	s="".join(s) 
	print("Without Order:",s) 
	t="" 
	for i in str: 
		if(i in t): 
			pass
		else: 
			t=t+i 
		print("With Order:",t) 
	
str="geeksforgeeks"
removeDuplicate(str)'''
#all the minimum frequencies in string and also max
'''# # Python 3 code to demonstrate 
# Least Frequent Character in String
# naive method 

# initializing string 
test_str = "GeeksforGeeks"

# printing original string
print ("The original string is : " + test_str)

# using naive method to get
# Least Frequent Character in String
all_freq = {}
for i in test_str:
if i in all_freq:
all_freq[i] += 1
else:
all_freq[i] = 1
res = min(all_freq, key = all_freq.get) 

# printing result 
print ("The minimum of all characters in GeeksforGeeks is : " + str(res))'''
#if string has special char
'''# Python code
# to check if any special character is present
# in a given string or not

# input string
n = "Geeks$For$Geeks"
n.split()
c = 0
s = '[@_!#$%^&*()<>?/\|}{~:]' # special character set
for i in range(len(n)):
	# checking if any special character is present in given string or not
	if n[i] in s:
		c += 1 # if special character found then add 1 to the c

# if c value is greater than 0 then print no
# means special character is found in string
if c:
	print("string is not accepted")
else:
	print("string accepted")

# this code is contributed by gangarajula laxmi'''
#avoid spaces
# Python3 code to demonstrate working of 
# Avoid Spaces in Characters Frequency
# Using sum() + len() + map() + split()

# initializing string
'''test_str = 'geeksforgeeks 33 is best'

# printing original string
print("The original string is : " + str(test_str))

# len() finds individual word Frequency 
# sum() extracts final Frequency
res = sum(map(len, test_str.split()))
	
# printing result 
print("The Characters Frequency avoiding spaces : " + str(res))'''
#words which are greater than given lenght
'''# Python program to find all string
# which are greater than given length k

# function find string greater than length k


def string_k(k, str):

	# create the empty string
	string = []

	# split the string where space is comes
	text = str.split(" ")

	# iterate the loop till every substring
	for x in text:

		# if length of current sub string
		# is greater than k then
		if len(x) > k:

			# append this sub string in
			# string list
			string.append(x)

	# return string list
	return string


# Driver Program
k = 3
str = "geek for geeks"
print(string_k(k, str))'''
#random string untill string get matched
'''# Python program to generate and match 
# the string from all random strings 
# of same length 

# Importing string, random 
# and time modules 
import string 
import random 
import time 

# all possible characters including 
# lowercase, uppercase and special symbols 
possibleCharacters = string.ascii_lowercase + string.digits +string.ascii_uppercase + ' ., !?;:'

# string to be generated 
t = "geek"

# To take input from user 
# t = input(str("Enter your target text: ")) 

attemptThis = ''.join(random.choice(possibleCharacters) 
								for i in range(len(t))) 
attemptNext = '' 

completed = False
iteration = 0

# Iterate while completed is false 
while completed == False: 
	print(attemptThis) 
	
	attemptNext = '' 
	completed = True
	
	# Fix the index if matches with 
	# the strings to be generated 
	for i in range(len(t)): 
		if attemptThis[i] != t[i]: 
			completed = False
			attemptNext += random.choice(possibleCharacters) 
		else: 
			attemptNext += t[i] 
			
	# increment the iteration 
	iteration += 1
	attemptThis = attemptNext 
	time.sleep(0.1) 

# Driver Code 
print("Target matched after " +
	str(iteration) + " iterations") '''

#



 


