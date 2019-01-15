import cv2
import os

def make_positive():

	pos_img = cv2.imread('index.jpeg', cv2.IMREAD_GRAYSCALE)

	resized_image = cv2.resize(pos_img , (50, 50))

	cv2.imwrite('index_pos_image.jpeg' , resized_image)


make_positive()
