import cv2
import os
import numpy as np
import urllib.request

def find_uglies():
	for file_type in ['neg']:
		for img in os.listdir(file_type):
			for ugly in os.listdir('uglies'):
				try:
					current_image_path = str(file_type)+ "/"+str(img)
					ugly = cv2.imread('uglies/' + str(ugly))
					question = cv2.imread(current_image_path)
					print("nehbj")

					if ugly.shape == question.shape and not(np.bitwise_xor(ugly , question).any()):
						print("ugly image!!!!!!!!!!")
						print(current_image_path)
						os.remove(current_image_path)

				except Exception as e:
					print(str(e))



find_uglies()
