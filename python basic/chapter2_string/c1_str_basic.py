'''String is a data type in python. 
String is a sequence of characters enclosed in quotes. 
We can primarily write a string in these three ways. '''

a ='harry1'       # Single quoted string 
b = "harry2"      # Double quoted string 
c = '''harry3'''  # Triple quoted string

print(a)
print(b)
print(c)

#STRING SLICING : A string in python can be sliced for getting a part of the strings. 
name ='akash'
length_str = len(name) # len() : find the length
print(length_str)
'''
The index in a sting starts from 0 to (length -1) in Python. In order to slice a string, we use 
the following syntax:
sl = name[start_indx: end_indx]
'''

sl1 = name[0:2]
print(sl1)

sl2 = name[1:4]
print(sl2)

sl3 = name[0:]
print(sl3)

sl4=name[:5]
print(sl4)

#SLICING WITH SKIP VALUE : sl[start:stop:step]
#step:The interval or "skip value" between elements.
str = '0123456789'
st1 = str[1:6:2]
print(st1)


