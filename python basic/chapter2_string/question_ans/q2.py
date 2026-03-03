# Write a program to detect double space in a string.

string1 = "akash is best"
string2 = "akash is  best"

# Method 1: Using 'in' operator
def has_double_space(text):
    return "  " in text

print("Method 1: Using 'in' operator")
print(f"'{string1}' has double space: {has_double_space(string1)}")
print(f"'{string2}' has double space: {has_double_space(string2)}")

# Method 2: Using count() method
print("\nMethod 2: Using count() method")
print(f"'{string1}' has double space: {string1.count('  ') > 0}")
print(f"'{string2}' has double space: {string2.count('  ') > 0}")

# Method 3: Show count of double spaces
print("\nMethod 3: Count number of double spaces")
print(f"'{string1}' - Number of double spaces: {string1.count('  ')}")
print(f"'{string2}' - Number of double spaces: {string2.count('  ')}")
