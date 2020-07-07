#this is just for easily renaming tons of text files at once

import os

dirName = '6'

def main():

	for fileNo, fileName in enumerate(os.listdir('/home/ubuntu/writerAuthentification/dataset-1/' + dirName)):

		destination = '/home/ubuntu/writerAuthentification/dataset-1' + '/' + dirName + '/' + str(fileNo) + '.docx'
		source = '/home/ubuntu/writerAuthentification/dataset-1' + '/' + dirName + '/' + str(fileName) 

		os.rename(source, destination)

		print("renamed file " + source + " to " + destination)


if __name__ == '__main__':

	print("initialized")

	main()

print("completed")




