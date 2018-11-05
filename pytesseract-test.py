import cv2
import sys
import pytesseract

def pre_process(image):
	# https://medium.freecodecamp.org/getting-started-with-tesseract-part-i-2a6a6b1cf75e

	# 0. Greyscaling the image
	image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# 1. Rescaling the image
	image = cv2.resize(image, None, fx = 1.5, fy = 1.5)

	# 2. Apply dilation
	kernel = np.ones((1, 1), np.uint8)
	image = cv2.dilate(image, kernel, iterations = 1)

	# 3. Apply erosion
	image = cv2.erode(image, kernel, iterations = 1)

	# 4. Apply gaussian blur to smooth out edges
	image = cv2.GaussianBlur(image, (5, 5), 0)

	# 5. Converting image to black and white
	# cv2.threshold returns (threshold, binary image) dict.
	image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

	return image

def main():

	# Program must require a command line argument
	if len(sys.argv) < 2:
		print('Usage: python pytesseract-test.py [image-file]')
		sys.exit(1)

	# Image path
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