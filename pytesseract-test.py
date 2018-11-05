import cv2
import sys
import pytesseract

def main():

	# Program must require a command line argument
	if len(sys.argv) < 2:
		print('Usage: python pytesseract-test.py [image-file]')
		sys.exit(1)

	# Image path
	imgPath = sys.argv[1]

	# Reading in the image
	image = cv2.imread(imgPath, cv2.IMREAD_COLOR)
	greyImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	(threshold, imageBinary) = cv2.threshold(greyImage, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

	# Arguments to use during recognition
	config = ('-l eng --oem 1 --psm 3')

	# Running tesseract
	textFound = pytesseract.image_to_string(
		imageBinary,
		config = config
	)

	print(textFound)

if __name__ == '__main__':
	main()