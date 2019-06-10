__author__ = "D1nz"

""" 
This program deletes all the conf.bin and depth.bin files in the raw_data.
The x-conf.bin files contain info about the orientation of the palm/hand.
The x-depth.bin files are binary files that can be converted as images.

Note: Use this program only after converting depth.bin to depth.jpg

"""

import os
from os import walk

f=[]

for (dirpath, dirnames, filenames) in walk("./raw_data"):
    f.extend(filenames)
    if(len(filenames)>0):
	    for i in range (len(filenames)):
	    	s = str(filenames[i])
	    	if(".bin" in s):
	    		os.remove(dirpath+"/"+filenames[i])

