__author__ = "D1nz"

"""
This program converts the binary files 'x-depth.bin' to jpg image

"""

import os
from os import walk
import numpy as np
import struct
import matplotlib.pyplot as plt

f=[]

for (dirpath, dirnames, filenames) in walk("./raw_data"):
    f.extend(filenames)
    if(len(filenames)>0):
	    for i in range (len(filenames)):
	    	s = str(filenames[i])
	    	if("depth" in s):
	    		fi = open(dirpath+"/"+filenames[i], "rb")
	    		img = fi.read()
	    		ig = struct.unpack("i" * ((len(img) -24) // 4), img[20:-4])
	    		plt.imshow(np.reshape(ig, [237, 162]))
	    		plt.savefig("hi.png")
	    		break
	    break    		