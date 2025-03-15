"""
List is another data type in coding - similar to integers, strings, 

defintion: within the square brackets, you can store multiple datas separated by commas
"""

# example 1 - a string list
shopping_list = ["apple", "banana", "crab", "donkey"]

# example 2 - an integer list
number_list = [1, 2, 3, 4]

# example 3 - a list within a list
# technically this is called a 2d matrix
list_list = [[1, 2, 3],  [4, 5, 6], [7, 8, 9]]

# list techniques
# tech 0 - get length of list
length = len(shopping_list)

# tech 1 - adding an item
# - adds "hello" to the end of the list
shopping_list.append("hello")

# t2 - print a specific item from the list
# index positions begin at 0
# the last index can be found at -1
item = shopping_list[0]
print(item)

# t3 - delete a specific item from the list
del shopping_list[-1]

# t4 - printing the list 
#   print the list variable
print(shopping_list)

# t5 - print each item in the list with a for loop
# tip:
#  range(1,6) == [1,2,3,4,5]
for item in shopping_list:
    print(item)

# t6 - print each item in the list with a while loop
i = 0
while i < len(shopping_list):
    print(shopping_list[i])
    i += 1
