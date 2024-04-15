#size of tuple
'''# sample Tuples
Tuple1 = ("A", 1, "B", 2, "C", 3)
Tuple2 = ("Geek1", "Raju", "Geek2", "Nikhil", "Geek3", "Deepanshu")
Tuple3 = ((1, "Lion"), ( 2, "Tiger"), (3, "Fox"), (4, "Wolf"))

# print the sizes of sample Tuples
print("Size of Tuple1: " + str(Tuple1.__sizeof__()) + "bytes")
print("Size of Tuple2: " + str(Tuple2.__sizeof__()) + "bytes")
print("Size of Tuple3: " + str(Tuple3.__sizeof__()) + "bytes")'''
#max and min k elements
'''# Python3 code to demonstrate working of 
# Maximum and Minimum K elements in Tuple
# Using slicing + sorted()

# initializing tuple
test_tup = (5, 20, 3, 7, 6, 8)

# printing original tuple
print("The original tuple is : " + str(test_tup))

# initializing K 
K = 2

# Maximum and Minimum K elements in Tuple
# Using slicing + sorted()
test_tup = list(test_tup)
temp = sorted(test_tup)
res = tuple(temp[:K] + temp[-K:])

# printing result 
print("The extracted values : " + str(res))'''
#create a list of tuples having its list having cubes
'''# Python program to create a list of tuples
# from given list having number and
# its cube in each tuple

# creating a list
list1 = [1, 2, 5, 6]

# using list comprehension to iterate each
# values in list and create a tuple as specified
res = [(val, pow(val, 3)) for val in list1]

# print the result
print(res)'''
#adding tuples to list
'''# Python3 code to demonstrate working of 
# Adding Tuple to List and vice - versa
# Using += operator (list + tuple)

# initializing list
test_list = [5, 6, 7]

# printing original list
print("The original list is : " + str(test_list))

# initializing tuple 
test_tup = (9, 10)

# Adding Tuple to List and vice - versa
# Using += operator (list + tuple)
test_list += test_tup

# printing result 
print("The container after addition : " + str(test_list))'''
#closest pair of kth element
'''# # Python3 code to demonstrate working of 
# Closest Pair to Kth index element in Tuple
# Using enumerate() + loop

# initializing list
test_list = [(3, 4), (78, 76), (2, 3), (9, 8), (19, 23)]

# printing original list
print("The original list is : " + str(test_list))

# initializing tuple
tup = (17, 23)

# initializing K 
K = 1

# Closest Pair to Kth index element in Tuple
# Using enumerate() + loop
min_dif, res = 999999999, None
for idx, val in enumerate(test_list):
	dif = abs(tup[K - 1] - val[K - 1])
	if dif < min_dif:
		min_dif, res = dif, idx

# printing result 
print("The nearest tuple to Kth index element is : " + str(test_list[res]))'''
#join tuples if similar initial element
'''## Python3 code to demonstrate working of
# Join Tuples if similar initial element
# Using loop

# initializing list
test_list = [(5, 6), (5, 7), (6, 8), (6, 10), (7, 13)]

# printing original list
print("The original list is : " + str(test_list))

# Join Tuples if similar initial element
# Using loop
res = []
for sub in test_list:
	if res and res[-1][0] == sub[0]:
		res[-1].extend(sub[1:])
	else:
		res.append([ele for ele in sub])
res = list(map(tuple, res))

# printing result
print("The extracted elements : " + str(res))'''
#extract digits from tuple list
'''# Python3 code to demonstrate working of
# Extract digits from Tuple list

# initializing list
test_list = [(15, 3), (3, 9), (1, 10), (99, 2)]

# printing original list
print("The original list is : " + str(test_list))
x=""
# Extract digits from Tuple list
for i in test_list:
	for j in i:
		x+=str(j)
res=list(map(int,set(x)))
# printing result
print("The extracted digits : " + str(res))'''
#all pairs combination of two tuples
'''# input
tuple1 = (4, 5)
tuple2 = (7, 8)

# initialize an empty list to store the filtered tuples
filtered_tuples = []

# iterate over each element in tuple 1
for element1 in tuple1:
	# iterate over each element in tuple 2
	for element2 in tuple2:
		# append a tuple of the two elements to the filtered list
		filtered_tuples.append((element1, element2))
		# append a tuple of the two elements in reverse order to the filtered list
		filtered_tuples.append((element2, element1))

# output
print(filtered_tuples)'''
#remove tuples of lenght k
'''# input
original_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
k = 1

# use map() and a lambda function to filter out tuples of length k
filtered_list = list(map(lambda x: x, filter(lambda x: len(x) != k, original_list)))

# output
print(filtered_list)'''
#sort a list of tuples by second item
'''# Python program to sort a list of tuples by the second Item

# Function to sort the list of tuples by its second item


def Sort_Tuple(tup):

	# getting length of list of tuples
	lst = len(tup)
	for i in range(0, lst):

		for j in range(0, lst-i-1):
			if (tup[j][1] > tup[j + 1][1]):
				temp = tup[j]
				tup[j] = tup[j + 1]
				tup[j + 1] = temp
	return tup


# Driver Code
tup = [('for', 24), ('is', 10), ('Geeks', 28),
	('Geeksforgeeks', 5), ('portal', 20), ('a', 15)]

print(Sort_Tuple(tup))'''
#ordered tuples by list
'''# Python3 code to demonstrate working of 
# Order Tuples by List
# Using dict() + list comprehension

# initializing list
test_list = [('Gfg', 3), ('best', 9), ('CS', 10), ('Geeks', 2)]

# printing original list
print("The original list is : " + str(test_list))

# initializing order list 
ord_list = ['Geeks', 'best', 'CS', 'Gfg']

# Order Tuples by List
# Using dict() + list comprehension
temp = dict(test_list)
res = [(key, temp[key]) for key in ord_list]

# printing result 
print("The ordered tuple list : " + str(res))'''
#flatten tuple of list of tuple
'''## Python3 code to demonstrate working of
# Flatten tuple of List to tuple
# Using sum() + tuple()

# initializing tuple
test_tuple = ([5, 6], [6, 7, 8, 9], [3])

# printing original tuple
print("The original tuple : " + str(test_tuple))

# Flatten tuple of List to tuple
# Using sum() + tuple()
res = tuple(sum(test_tuple, []))

# printing result
print("The flattened tuple : " + str(res))'''
#convert nested cuples to key dict
'''# Python3 code to demonstrate working of 
# Convert Nested Tuple to Custom Key Dictionary 
# Using list comprehension + dictionary comprehension 

# initializing tuple 
test_tuple = ((4, 'Gfg', 10), (3, 'is', 8), (6, 'Best', 10)) 

# printing original tuple 
print("The original tuple : " + str(test_tuple)) 

# Convert Nested Tuple to Custom Key Dictionary 
# Using list comprehension + dictionary comprehension 
res = [{'key': sub[0], 'value': sub[1], 'id': sub[2]} 
							for sub in test_tuple] 

# printing result 
print("The converted dictionary : " + str(res))''' 

 

# def apply_pattern(input_str, num_rows):
#     pattern = [''] * num_rows
#     row = 0
#     direction = 1
 
#     for char in input_str:
#         pattern[row] += char
#         if row == 0:
#             direction = 1
#         elif row == num_rows - 1:
#             direction = -1
#         row += direction
 
#     return ''.join(pattern)
 
# # Example usage:
# input_str = input()
# num_rows = int(input())
# output_str = apply_pattern(input_str, num_rows)
# print(output_str)


#The tutorial practice
'''n="hello"
k=n[:]
print(k + " hi")'''

'''f="raji"
l="sreepathi"
print(f + l + " is a coder")#also f +'['+l+ '] is a coder'''
i=1
while i<=5:
    print("*" * i)
    i=i-1
print(i)


 
 



