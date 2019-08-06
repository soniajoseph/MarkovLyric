import string, random, sys

# create Markov model of order k for specified text
def markovModel(text, k):
	# make circular
	start = text[0:k]
	text = " ".join([text, start])
	kgrams = {}
	for i in range(0, len(text)-k, 1):
		key = text[i:i+k] # kgram
		char = text[i+k] # next character
		# put in kgram table
		if key not in kgrams:
			kgrams[key] = {}
		if char not in kgrams[key]:
			kgrams[key][char] = 1
		else:
			kgrams[key][char] += 1
	return kgrams

# get next character in model by weighted probability
def nextCharacter(kgrams, key):
	choice = []
	for letter in kgrams[key]:
		for count in range(0, kgrams[key][letter], 1):
			choice.append(letter)
	return random.choice(choice)

# generate text
def textGenerator(text, k, characters):
	kgrams = markovModel(text, k)
	starting_kgram = text[0:k]
	for i in range(0, characters, 1):
		# print character
		char = nextCharacter(kgrams, starting_kgram)
		print(char,end='')
		# update kgram
		starting_kgram = starting_kgram[1:] # remove first character
		starting_kgram = "".join([starting_kgram,char])# add new character

if __name__ == "__main__":
	f = open(sys.argv[1],"r")
	text = f.read()
	textGenerator(text, int(sys.argv[2]), int(sys.argv[3]))
	print()
