
def count(text, let):
	counter = 0
	# print(let)
	for c in text:
		if c == let:
			counter+=1
	return counter

text = open("study-guide.txt", 'r').read()

frequency_dictionary = {}

for c in text :
	if not (c in frequency_dictionary) and c.isalpha():
		frequency_dictionary[c] = count(text, c)

for c in sorted(frequency_dictionary, key = frequency_dictionary.get, reverse=True):
	print(c , ' : ' , frequency_dictionary[c])


# TODO :
	# match each letter with the english frequency table