'''
	Program summary : Minimum distance between two elements in array
	Input: List,Number1,Number2
'''

import ast

li = ast.literal_eval(input("enter the list:-"))
a = int(input("Enter the first number:-"))
b = int(input("Enter the second number:-"))

arr1 = []
arr2 = []

# Find the occurences of first and second number
for i in range(len(li)):
    if a == li[i]:
        arr1.append(i)

    if b == li[i]:
        arr2.append(i)

if (len(arr1) == 0) or (len(arr2) == 0):
	t = 'Please enter a valid number from the list'
else:
	t = min([abs(i - j) for i in arr1 for j in arr2])
	
print(t)
        
