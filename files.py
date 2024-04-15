'''import os

def create_file(filename):
	try:
		with open(filename, 'w') as f:
			f.write('Hello, world!\n')
		print("File " + filename + " created successfully.")
	except IOError:
		print("Error: could not create file " + filename)

def read_file(filename):
	try:
		with open(filename, 'r') as f:
			contents = f.read()
			print(contents)
	except IOError:
		print("Error: could not read file " + filename)

def append_file(filename, text):
	try:
		with open(filename, 'a') as f:
			f.write(text)
		print("Text appended to file " + filename + " successfully.")
	except IOError:
		print("Error: could not append to file " + filename)

def rename_file(filename, new_filename):
	try:
		os.rename(filename, new_filename)
		print("File " + filename + " renamed to " + new_filename + " successfully.")
	except IOError:
		print("Error: could not rename file " + filename)

def delete_file(filename):
	try:
		os.remove(filename)
		print("File " + filename + " deleted successfully.")
	except IOError:
		print("Error: could not delete file " + filename)


if __name__ == '__main__':
	filename = "example.txt"
	new_filename = "new_example.txt"

	create_file(filename)
	read_file(filename)
	append_file(filename, "This is some additional text.\n")
	read_file(filename)
	rename_file(filename, new_filename)
	read_file(new_filename)
	delete_file(new_filename)'''
#line by line 
'''fin=open("C://Users/SREEPATHIR/Documents/lava/data.txt")
for i in fin:
    print(i.split())
    for w in i.split():print(w)'''
#charecter by charecter
'''fin=open("C://Users/SREEPATHIR/Documents/lava/data.txt")
for i in fin:
    for w in i:print(w)'''
#no.of charecter,words,spaces and lines
# Function to count number of characters, words, spaces and lines in a file
'''def counter(fname):

	# variable to store total word count
	num_words = 0
	
	# variable to store total line count
	num_lines = 0
	
	# variable to store total character count
	num_charc = 0
	
	# variable to store total space count
	num_spaces = 0
	
	# opening file using with() method
	# so that file gets closed
	# after completion of work
	with open(fname, 'r') as f:
		
		# loop to iterate file
		# line by line
		for line in f:
			
			# incrementing value of num_lines with each
			# iteration of loop to store total line count
			num_lines += 1
			
			# declaring a variable word and assigning its value as Y
			# because every file is supposed to start with a word or a character
			word = 'Y'
			
			# loop to iterate every
			# line letter by letter
			for letter in line:
				
				# condition to check that the encountered character
				# is not white space and a word
				if (letter != ' ' and word == 'Y'):
					
					# incrementing the word
					# count by 1
					num_words += 1
					
					# assigning value N to variable word because until
					# space will not encounter a word can not be completed
					word = 'N'
					
				# condition to check that the encountered character is a white space
				elif (letter == ' '):
					
					# incrementing the space
					# count by 1
					num_spaces += 1
					
					# assigning value Y to variable word because after
					# white space a word is supposed to occur
					word = 'Y'
					
				# loop to iterate every character
				for i in letter:
					
					# condition to check white space
					if(i !=" " and i !="\n"):
						
						# incrementing character
						# count by 1
						num_charc += 1
						
	# printing total word count
	print("Number of words in text file: ",
		num_words)
	
	# printing total line count
	print("Number of lines in text file: ",
		num_lines)
	
	# printing total character count
	print('Number of characters in text file: ',
		num_charc)
	
	# printing total space count
	print('Number of spaces in text file: ',
		num_spaces)
	
# Driver Code:
if __name__ == '__main__':
	fname = 'File1.txt'
	try:
		counter(fname)
	except:
		print('File not found')'''
#words containing no.of charecters
'''def find_words_with_three_chars(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        words = content.split()
 
        words_with_three_chars = [word for word in words if len(word) == 3]
 
        return words_with_three_chars
 
file_name = "File1.txt"
result = find_words_with_three_chars(file_name)
 
print("Words containing three characters:")
print(result)'''
#target word in which line
'''def find_word_line_number(filename, target_word):
	line_number = 0

	with open(filename, 'r') as file:
		for line in file:
			line_number += 1
			if target_word in line:
				return line_number

	# If the word is not found in the file, return None
	return None

# Example usage
filename = "File1.txt" # Replace with the name of your file
word_to_find = "hello" # Replace with the word you want to find
line_number = find_word_line_number(filename, word_to_find)
if line_number is not None:
	print(f"The word '{word_to_find}' is present in line number: {line_number}")
else:
	print(f"The word '{word_to_find}' is not found in the file.")'''
#count no.of lines
'''fin=open("C://Users/SREEPATHIR/Documents/lava/data.txt")
c=0
for i in fin:
    c+=1
print(c)'''
#if line starts with
'''file1 = open('GeeksforGeeks.txt','r')

# defining object file2 to open GeeksforGeeksUpdated file in write mode
file2 = open('GeeksforGeeksUpdated.txt','w')

# reading each line from original text file
for line in file1.readlines():

	# reading all lines that do not begin with "TextGenerator"
	if not (line.startswith('TextGenerator')):
	
		# printing those lines
		print(line)
		
		# storing only those lines that 
		# do not begin with "TextGenerator"
		file2.write(line)

# close and save the files
file2.close()
file1.close()'''
#remove duplicate lines
'''def remove_duplicates(input_file, output_file):
	lines_seen = set()
	with open(output_file, 'w') as out_file:
		with open(input_file, 'r') as in_file:
			for line in in_file:
				if line not in lines_seen:
					out_file.write(line)
					lines_seen.add(line)

# Usage
input_file = open('C:/Users/user/Desktop/Lorem_input.txt', "r")
output_file = open('C:/Users/user/Desktop/Lorem_output.txt', "w")
remove_duplicates(input_file, output_file)'''
#read list of dict files
'''def parse(d):
	dictionary = dict()
	# Removes curly braces and splits the pairs into a list
	pairs = d.strip('{}').split(', ')
	for i in pairs:
		pair = i.split(': ')
		# Other symbols from the key-value pair should be stripped.
		dictionary[pair[0].strip('\'\'\"\"')] = pair[1].strip('\'\'\"\"')
	return dictionary
try:
	geeky_file = open('geeky_file.txt', 'rt')
	lines = geeky_file.read().split('\n')
	for l in lines:
		if l != '':
			dictionary = parse(l)
			print(dictionary)
	geeky_file.close()
except:
	print("Something unexpected occurred!")'''
#append the content from one text file to another
'''# entering the file names
firstfile = input("Enter the name of first file ")
secondfile = input("Enter the name of second file ")

# opening both files in read only mode to read initial contents
f1 = open(firstfile, 'r')
f2 = open(secondfile, 'r')

# printing the contents of the file before appending
print('content of first file before appending -', f1.read())
print('content of second file before appending -', f2.read())

# closing the files
f1.close()
f2.close()

# opening first file in append mode and second file in read mode
f1 = open(firstfile, 'a+')
f2 = open(secondfile, 'r')

# appending the contents of the second file to the first file
f1.write(f2.read())

# relocating the cursor of the files at the beginning
f1.seek(0)
f2.seek(0)

# printing the contents of the files after appendng
print('content of first file after appending -', f1.read())
print('content of second file after appending -', f2.read())

# closing the files
f1.close()
f2.close()'''
#append file for odd lines
'''def copy_odd_lines(input_file, output_file):
	with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
		for line_number, line in enumerate(infile, 1):
			if line_number % 2 != 0:
				outfile.write(line)

# Example usage:
input_file_name = 'input.txt'
output_file_name = 'output.txt'
copy_odd_lines(input_file_name, output_file_name)'''
#copy two files data into another
'''data = data2 = "";

# Reading data from file1
with open('file1.txt') as fp:
	data = fp.read()

# Reading data from file2
with open('file2.txt') as fp:
	data2 = fp.read()

# Merging 2 files
# To add the data of file2
# from next line
data += "\n"
data += data2

with open ('file3.txt', 'w') as fp:
	fp.write(data)'''
#reverse a each line of code
# Open file in read mode
'''f = open('GFG.txt', 'r')

# Read the content of the
# file and store it in a list
lines = f.readlines()
	
# Close file
f.close()

# User's choice
choice = 1

# Split the line into words 
line = lines[choice].split()

# line is reversed
Reversed = " ".join(line[::-1])

# Updating the content of the
# file
lines.pop(choice)
lines.insert(choice, Reversed)'''
#reverse entire file and store it in another file
# Open the file in write mode
'''f1 = open("output1.txt", "w")

# Open the input file and get 
# the content into a variable data
with open("file.txt", "r") as myfile:
	data = myfile.read()

# For Full Reversing we will store the 
# value of data into new variable data_1 
# in a reverse order using [start: end: step],
# where step when passed -1 will reverse 
# the string
data_1 = data[::-1]

# Now we will write the fully reverse 
# data in the output1 file using 
# following command
f1.write(data_1)

f1.close()


# Open file in write mode
u = open('GFG.txt', 'w')

# Write the new content in file
# and note, it is overwritten 
u.writelines(lines)
u.close()'''
#reverse the content of file using stack
# Creating Stack class (LIFO rule)
'''class Stack:

	def __init__(self):

		# Creating an empty stack
		self._arr = []

	# Creating push() method.
	def push(self, val):
		self._arr.append(val)

	def is_empty(self):

		# Returns True if empty
		return len(self._arr) == 0

	# Creating Pop method.
	def pop(self):

		if self.is_empty():
			print("Stack is empty")
			return

		return self._arr.pop()

# Creating a function which will reverse
# the lines of a file and Overwrites the
# given file with its contents line-by-line
# reversed


def reverse_file(filename):

	S = Stack()
	original = open(filename)

	for line in original:
		S.push(line.rstrip("\n"))

	original.close()

	output = open(filename, 'w')

	while not S.is_empty():
		output.write(S.pop()+";\n")

	output.close()


# Driver Code
filename = "GFG.txt"

# Calling the reverse_file function
reverse_file(filename)

# Now reading the content of the file
with open(filename) as file:
	for f in file.readlines():
		print(f, end="")'''












