import os
import spacy
import numpy as np
import docx2txt
import collections

homeDir = '/home/ubuntu/writerAuthentification/dataset-1/'

def convertToPOS(text):
#Converts text to POS using spacy. This particular method ignores punctuation and spaces

	posText = ""
	nlp = spacy.load("en_core_web_sm")
	doc = nlp(str(text))

	for token in doc:

		if not(token.pos_ == 'SPACE' or token.pos_ == 'PUNCT'):

			posText = posText + " " + token.pos_ 
		
	return posText

def identifyMostCommonGrams(text, N, X):
	mostFrequentGrams = np.empty(X)

	amountOfNGrams = len(text.split()) - (N-1)
	gramArray = ['','']
	individualWordsList = text.split()
	gramWordsList = []
	for i in range(amountOfNGrams):
		gramWordsList.append(0)
	gramFrequencyList = []
	for i in range(amountOfNGrams):
		gramFrequencyList.append(0)

	#print(individualWordsList)

	for q in range(len(individualWordsList)-(N-1)):

		temp = ""

		for i in range(N):

			temp = temp + individualWordsList[i + q] + " "

		gramWordsList[q] = temp

	#print(gramWordsList)

	counter = collections.Counter(gramWordsList)
	print(counter.most_common(X))

def main():


	for dirNo, dirName in enumerate(sorted(os.listdir(homeDir)), start = 1):
		#traverse directory
		#print("Directory " + dirName + ", number " + str(dirNo) + " recognized")
		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		for fileNo, fileName in enumerate(sorted(os.listdir(homeDir + dirName)), start = 1):
			#traverse file in directory
			#print("		File " + fileName + " from directory " + dirName + " recognized")
			#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
			if fileName.endswith('txt'):

				with open(homeDir + dirName + "/" + fileName, 'r', encoding = 'utf-8', errors = 'ignore') as f:

					print("Top 5 most common plaintext 3-grams in " + fileName + " of directory " + dirName + " are " + identifyMostCommonGrams(f.read(), 3, 5))

					print("Top 5 most common POS 3-grams in " + fileName + " of directory " + dirName + " are " + identifyMostCommonGrams(convertToPOS(f.read())))

			elif fileName.endswith('docx'):

				currentFile = docx2txt.process(homeDir + dirName + "/" + fileName)

				print("Top 5 most common plaintext 3-grams in " + fileName + " of directory " + dirName + " are ")# + identifyMostCommonGrams(str(currentFile), 3, 5))

				print("Top 5 most common POS 3-grams in " + fileName + " of directory " + dirName + " are ")# + identifyMostCommonGrams(convertToPOS(str(currentFile)), 3, 5))

			else:
				print("invalid doctype!")




	

if __name__ == '__main__':

	print("initialized")

	main()

print("completed")

