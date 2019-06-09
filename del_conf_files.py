__author__ = "D1nz"

""" 
This program deletes all the conf.bin files in the raw_data.
The x-conf.bin files contain info about the orientation of the palm/hand.

"""

import os
from os import walk

f=[]

for (dirpath, dirnames, filenames) in walk("./raw_data"):
    f.extend(filenames)
    if(len(filenames)>0):
	    for i in range (len(filenames)):
	    	s = str(filenames[i])
	    	if("conf" in s):
	    		os.remove(dirpath+"/"+filenames[i])

