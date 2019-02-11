f=open('words.txt')
pattern_string = 'a'
replacement_string ='the'
data = f.read()
print(data)
words = data.split()
print(words)
length_of_words =len(words)
print(length_of_words)
for i in  range(length_of_words):
	if words[i] == pattern_string:
		words[i] = replacement_string
		i=i+1
print(words)
data=' '.join(words)
f1=open('changes.txt', "w")
f1.write(data)
