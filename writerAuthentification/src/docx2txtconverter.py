#this is a utility I made just to convert docx files to .txt because .txt is so much easier to work with

import docx2txt
import os

dirName = "6"

def main():

	for fileNo, fileName in enumerate(os.listdir('/home/ubuntu/writerAuthentification/dataset-1/' + dirName)):

		DOCX_REPLACED = docx2txt.process("/home/ubuntu/writerAuthentification/dataset-1/" + dirName + "/" + fileName)

		with open("/home/ubuntu/writerAuthentification/dataset-1/" + dirName + "/" + str(fileNo) + '.txt', 'w') as text_file:

			print(DOCX_REPLACED)
			print(text_file)

if __name__ == '__main__':

	print("initialized")

	main()

print("completed")