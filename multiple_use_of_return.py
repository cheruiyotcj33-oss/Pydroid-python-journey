#asks the user for a number

n = int(input("enter no: "))

#we define the function
def double(n):
#we return double the number (n)
    return n + n
 
#results is given
result = double(n)
    
#asks the user for a number (p)
p = int(input("Enter no: "))

#defines "cube" function
def cube(p):

#returns the cube of the number given
       return p*p*p

#results given
results = cube(p)

#asks the user for two numbers
a = int(input("enter first no: "))
b = int(input("enter second no: "))

#defines the "add" function
def add(a , b):
#returns sum
    return a + b
#results given
Results = add(a , b)

#output result
print("double = " , result)
print("cube = " , results)
print("Sum = " , Results)