# -*- coding: utf-8 -*-

# ! /usr/local/Cellar/python3/3.6.1

# USAGE
# python3 selective_copy_021818_1.py

import os, re, shutil

#####################################
# USER INPUT
#####################################

# get user inputted folder path (as a string)

user_folder_input = input("Please provide the path to the folder you want to search:  ")

# get user inputted file extension (as a string)

user_file_ext_input = input("Please provide the file extension of the files you want to copy (formats should be written as .pdf, .jpg, .doc, etc.):  ")

#####################################
# END USER INPUT
#####################################


#####################################
# REGEX
#####################################

# create a regex statement to match `user_file_ext_input`
# https://regexr.com/3kvi4
# re.compile should turn a raw string into current regex language so you can skip creating the formula sort of...
# file_type_regex1 = re.compile(user_file_ext_input) # using this one will find files like `testFile.txt.doc` which is wrong
file_type_regex1 = re.compile(user_file_ext_input + "$")
# print(file_type_regex1) # for testing
# print(file_type_regex1.search("testTextA1.txt")) # for testing

#####################################
# END REGEX
#####################################


# walk through the folder tree, search for files with user chosen file extension
# os.walk() handles all the behind the scenes looping, including into the subfolders (without having to write a separate loop)

abs_cwd_file_path = os.path.abspath('.') # set the destination file path to be the current working directory or cwd
search_result_path = os.mkdir(os.path.join(abs_cwd_file_path,"search_results")) # os.path.join() will handle the `/` or `\` depending on OS

for foldername,subfolders,filenames in os.walk(user_folder_input):
	for filename in filenames:
		# print(filename) # for testing
		if file_type_regex1.search(filename):
			# print("Found a file with the %s ending." % (user_file_ext_input))
			print("Copying file: %s" % (filename))
			# use `os.path.join()` to create correct path rather than string concatenation
			src_file_path_name = os.path.abspath(os.path.join(user_folder_input,filename))
			dst_file_path_name = os.path.join(search_result_path,filename)
			# copy the files from their current location into a new folder (see Scratch file for thoughts on where new folder should be)
			# using `copyfile(src, dst)`
			copyfile(src_file_path_name, dst_file_path_name)
			

