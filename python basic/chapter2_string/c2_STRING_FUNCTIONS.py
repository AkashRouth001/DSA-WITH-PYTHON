# don't use `str` as a variable name because it shadows the built-in
text = 'akash'

# 1. len() function – returns the length of the string
print("length is =", len(text))

#2. String.endswith("rry") – This function_ tells whether the variable string ends with 
    #the string "rry" or not. 
print(text.endswith("sh"))
print(text.endswith("xx"))

#3. string.count("c") – counts the total number of occurrences of any character. 
print(text.count("a"))
print(text.count("k"))

#4.string.capitalize() = make capital the 1st letter of the word
print(text.capitalize()) 
text2 = "i am akash"
print(text2.capitalize())

#5. string.find(word) – This function friends a word and returns the index of first 
    #occurrence of that word in the string. 

print(text.find("k"))
print(text.find("a")) 

#6.string.replace (old word, new word ) – This function replace the old word with 
   #new word in the entire string.
re_text = text.replace('a','t')
print(re_text)