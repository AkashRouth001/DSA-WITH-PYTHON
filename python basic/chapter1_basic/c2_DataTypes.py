#Data type:
'''
Primarily these are the following data types in Python: 
1. Integers 
2. Floating point numbers 
3. Strings 
4. Booleans  
5. None 
'''
a = 10 #int
b= 10.1 # float
c= 'akash' # string
d = True # booleans

#OPERATORS IN PYTHON 
'''
Following are some common operators in python: 
1. Arithmetic operators: +, -, *, / etc. 
2. Assignment operators:  =, +=, -= etc. 
3. Comparison operators: ==, >, >=, <,  != etc. 
4. Logical operators: and, or, not.
'''

#TYPE() FUNCTION : type() function is used to find the data type of a given variable in python. 
aa = 10 #int
print(type(aa))
bb= 10.1 # float
print(type(bb))
cc= 'akash' # string
print(type(cc))
dd = True # booleans
print(type(dd))
print()


#TYPECASTING : Typecasting is converting a value from one data type to another
num = 10
print(num,"is",type(num))
flo = str(num)
print(flo,"is",type(flo))
string = float(num)
print(string,"is",type(string))