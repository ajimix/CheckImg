#!/usr/bin/python

# You should install Imaging module for Python
# http://www.pythonware.com/products/pil/

from PIL import Image
import sys, glob, os

# Change here the images to check
for file in glob.glob("*.jpg"):
	try:
		im = Image.open(file)
		im.verify()
	except IOError:
		# What to do with errors. Right now just print the file name
		print file