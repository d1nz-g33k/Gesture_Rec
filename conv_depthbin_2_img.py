__author__ = "D1nz"

"""
This program converts the binary files 'x-depth.bin' to jpg image

"""

import os
from os import walk
import numpy as np
import struct
import matplotlib.pyplot as plt
from oct2py import Oct2Py
oc = Oct2Py()

f=[]

script = "function y = depth(path, fisave)\n" \
         "    depth_filename = path;\n" \
         "	  inp = fopen(depth_filename,'rb');\n" \
		 "    img = fread(inp,320*240,'int16');\n" \
		 "    fclose(inp);\n" \
		 "    img = reshape(img,[320,240])';\n" \
		 "    img(img > 10000) = 0; % Set 0 if the pixel of distance is too far.\n" \
		 "    imwrite(img / max(max(img)), fisave);\n" \
         "end"

with open("depth.m","w+") as fi:
    fi.write(script)

for (dirpath, dirnames, filenames) in walk("./raw_data"):
	f.extend(filenames)
	if(len(filenames)>0):
		for i in range (len(filenames)):
			s = str(filenames[i])
			if("depth.bin" in s):
				path = str(dirpath+"\\"+filenames[i])
				filename, file_extension = os.path.splitext(path)
				fisave = str(filename + ".jpg")
				oc.depth(path, fisave)

