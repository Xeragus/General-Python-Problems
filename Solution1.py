#function to count the occurrences of each word in the sentence
def word_count(sentence):

	#split the sentence into words
	words = sentence.split()
	#define the dictionary that we are going to need for
	#storing the words and the number of times they occurre in the sentence
	occurrences = dict()

	#we need to see if the last word has something other then letters
	#it can has '.', '!' or '?'
	last_word = words[len(words)-1]
	#if there is something else besides letters then get the letters only
	if not last_word.isalpha():
		words[len(words)-1] = last_word[:(len(last_word)-1)]

	#initialize the dictionary from the words in the sentence
	initialize_dictionary(occurrences, words)

	#printing the occurences
	print_dictionary(occurrences)

	#analyzing the dictionary
	analyze_dictionary(occurrences)
	
	return occurrences

#initialize the dictionary with words and number of occurrences
def initialize_dictionary(occurrences, words):
	for word in words:
		if word.lower() in occurrences:
			occurrences[word] += 1
		else:
			occurrences[word.lower()] = 1

def analyze_dictionary(occurrences):
	for word in occurrences.keys():
		#transforming the words that occured only once in uppercase
		if occurrences[word] == 1:
			occurrences[word.upper()] = occurrences.pop(word)
		#transforming the words that occured twice in the specified
		#combination in the text
		elif occurrences[word] == 2:
			new_key = word[:2] + word[-2:]
			occurrences[new_key] = occurrences.pop(word)
		return occurrences

def print_dictionary(occurrences):
	for word in occurrences.keys():
		print('Total occurrences of the word \"{0}\": {1}'
			.format(word, occurrences[word]))

#input the sentence
sentence = input("Write a sentence: ").lower()
print(word_count(sentence))
