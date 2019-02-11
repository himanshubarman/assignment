'''
    Program summary : To print the patter
        1
        22
        33
        44
        33
        22
        1
'''
n = int(input('Please enter the number'))

def pattern(n):
    '''
        Function to print the pattern
    '''
    for i in n:
        if i == 1:
            print("{0}".format(i))
        else:
            print("{0}{1}".format(i,i))

# Function call
pattern(range(1,n))
pattern(range(n,0,-1))
