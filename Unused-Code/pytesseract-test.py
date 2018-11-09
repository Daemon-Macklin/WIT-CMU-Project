import cv2
import sys
import pytesseract
import numpy as np

def pre_process(image):

	# https://medium.freecodecamp.org/getting-started-with-tesseract-part-i-2a6a6b1cf75e

	# 0. Greyscaling the image
	image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# 1. Rescaling the image
	image = cv2.resize(image, None, fx = 2, fy = 2, interpolation = cv2.INTER_CUBIC)

	# 2. Apply dilation
	kernel = np.ones((1, 1), np.uint8)
	image = cv2.dilate(image, kernel, iterations = 1)

	# 3. Apply erosion
	image = cv2.erode(image, kernel, iterations = 1)

	# 4. Apply gaussian blur to smooth out edges
	# image = cv2.GaussianBlur(image, (5, 5), 0)
	image = cv2.bilateralFilter(image, 9, 75, 75)

	# 5. Converting image to black and white
	# cv2.threshold returns (threshold, binary image) dict.
	# image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
	image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

	return image

def main():

	# Getting the image path as a command line argument or input
	if len(sys.argv) < 2:
		print("Usage: python2 pytesseract-test.py [image]")
		sys.exit(1)

	imgPath = sys.argv[1]

	# Reading in the image and performing noise removal
	image = cv2.imread(imgPath, cv2.IMREAD_COLOR)
	image = pre_process(image)

	# Running tesseract
	textFound = pytesseract.image_to_string(
		image,

		# Arguments to use during recognition
		config = ('-l eng --oem 1 --psm 3')
	)

	print(textFound)

if __name__ == '__main__':
	main()