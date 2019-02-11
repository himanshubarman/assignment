'''
	Program Summary: Reverse the vowels in the string
	Input = string 
'''

input_string = input('Please enter a string')
vowel_list = ["a","e","i","o","u"]

t = [i for i in input_string if i in vowel_list]

if len(t) == 0:
	print('No vowels present in the list')

else:
	s = ''.join(t)
	print(s[::-1])
