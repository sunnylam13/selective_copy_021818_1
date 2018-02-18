# -*- coding: utf-8 -*-

# ! /usr/local/Cellar/python3/3.6.1

# USAGE
# ???

import os, re

#####################################
# USER INPUT
#####################################

# get user inputted folder path (as a string)

user_folder_input = input("Please provide the path to the folder you want to search:  ")

# get user inputted file extension (as a string)

user_file_ext_input = input("Please provide the file extension of the files you want to copy (formats should be written as pdf, jpg, doc, etc.  Don't use .jpg for example.):  ")

#####################################
# END USER INPUT
#####################################


#####################################
# REGEX
#####################################

# create a regex statement to match `user_file_ext_input`
# https://regexr.com/3kvi4
# re.compile should turn a raw string into current regex language
file_type_regex1 = re.compile('r' + "\'." + user_file_ext_input + "\'")
print(file_type_regex1) # for testing

#####################################
# END REGEX
#####################################


# walk through the folder tree, search for files with user chosen file extension
# os.walk() handles all the behind the scenes looping, including into the subfolders (without having to write a separate loop)

for foldername,subfolders,filenames in os.walk(user_folder_input):
	for filename in filenames:
		if file_type_regex1.search(filename):
			print("Found a file with the %s ending." % (user_file_ext_input))



# copy the files from their current location into a new folder (see Scratch file for thoughts on where new folder should be)