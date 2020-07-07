#The purpose of this is just to test my gram rater

import numpy as np
import collections

def identifyMostCommonGrams(text, N, X):
#N specifies the word length of the gram
#text is the string to be analyzed
#Method returns the top X most common N grams in the text string

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

	print(individualWordsList)

	for q in range(len(individualWordsList)-(N-1)):

		temp = ""

		for i in range(N):

			temp = temp + individualWordsList[i + q] + " "

		gramWordsList[q] = temp

	#All arrays initialized, time to analyze the text and return the most frequent N grams
	#this creates an array with the number of times each gram appears in cells corresponding to that gram
	#for g in range(len(gramWordsList)):
	#	tempIdentifier = gramWordsList[g]
#
#		for i in range(len(gramWordsList)):
#			if(tempIdentifier == gramWordsList[i]):
#				gramFrequencyList[g] += 1 

	#This part returns the top X most common grams

#	print("The most common gram is " + max(set(gramWordsList), key = gramWordsList.count)


	print(gramWordsList)

	counter = collections.Counter(gramWordsList)
	print(counter.most_common(2))


def main():

	identifyMostCommonGrams("i like eating cheese i like eating cheese", 3, 5)

if __name__ == '__main__':

	print("initialized")

	main()

print("completed")