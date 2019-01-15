import cv2
import urllib.request
import numpy as np
import os


def create_pos_neg():
	for filetype in ['neg']:
		for img in os.listdir(filetype):
			if filetype == 'neg':
				line = filetype + "/" + img + "\n"
				with open('bg.txt' , 'a') as f:  ## a = = append file handling
					f.write(line)


			elif filetype == 'pos':
				line = filetype+'/'+img+'1 0 0 50 50\n'
				with open('info.dat' , 'a') as f:
					f.write(line)

create_pos_neg()