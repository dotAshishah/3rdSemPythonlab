# 3a) Write a Python program that accepts a sentence and find the number of words, digits, 
# uppercase letters, and lowercase letters. 


sentence = input("Enter a sentence: ")
words = digits = upper = lower = 0
# Splitting the sentence using split() method , by default split is by spaces
# Return value - list of strings
split_sentence = sentence.split()
print("The result of split() on input sentence is : \n"+str(split_sentence)+"\n")
words = len(split_sentence )
for c in sentence:
 if c.isdigit():
 digits = digits + 1
 elif c.isupper():
 upper = upper + 1
 elif c.islower():
 lower = lower + 1
print ("No of Words: ", words)
print ("No of Digits: ", digits)
print ("No of Uppercase letters: ", upper)
print ("No of Lowercase letters: ", lower)



# OUTPUT:
# Enter a sentence: Rama went to Devaraja market to pick 2 kgs of vegetable
# The result of split() on input sentence is : 
# ['Rama', 'went', 'to', 'Devaraja', 'market', 'to', 'pick', '2', 'kgs', 'of', 'vegetable']
# No of Words: 11
# No of Digits: 1
# No of Uppercase letters: 2
# No of Lowercase letters: 42
