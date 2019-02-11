import re

file = open('words.txt')

#read() reads the file contents. 
text = (file.read())

#remove punctutaion from the text.
text= re.sub('[^\w\s]','',text)

#lower() converts  text to lowercase.
text=text.lower()

# split() returns list of all the words in the text.
words = text.split()
print(words)

