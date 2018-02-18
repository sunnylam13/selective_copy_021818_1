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

#####################################
# FILE ANALYSIS
#####################################

# walk through the folder tree, search for files with user chosen file extension
# os.walk() handles all the behind the scenes looping, including into the subfolders (without having to write a separate loop)

# get the absolute file path of the current working directory of program
abs_cwd_file_path = os.path.abspath('.') # set the destination file path to be the current working directory or cwd

# a list of all folders and subfolders to be analyzed
folder_path_list = [] # a list to hold all finalized folder paths (not folder names)


# create the search_result folder to store the copied files

if (os.path.join(abs_cwd_file_path,"search_results")): # if the search_results folder already exists
	search_result_path = (os.path.join(abs_cwd_file_path,"search_results")) # os.path.join() will handle the `/` or `\` depending on OS
	# simply set the path to the search_results folder...
else: # otherwise create the folder and then set search_result_path
	search_result_path = os.mkdir(os.path.join(abs_cwd_file_path,"search_results")) # os.path.join() will handle the `/` or `\` depending on OS
	search_result_path = (os.path.join(abs_cwd_file_path,"search_results")) # os.path.join() will handle the `/` or `\` depending on OS
	# simply set the path to the search_results folder...

def find_abs_src_path(path,filename):
	# SOURCE FILE
	# get the directory path leading to the file name for later source copying
	# we need to do this rather than using `user_folder_input` otherwise we'll miss subfolders and get errors
	# use `os.path.join()` to create correct path rather than string concatenation
	# use os.path.abspath() to make sure it's an absolute path
	
	# src_file_path_name = os.path.abspath(os.path.join(user_folder_input,filename))
	src_file_path_name = os.path.abspath(os.path.join(path,filename))

	return src_file_path_name

def find_abs_dst_path(path,filename):
	# dst_file_path_name = os.path.join(search_result_path,filename + "_" + "copy")
	dst_file_path_name = os.path.join(path,filename + "_" + "copy")

	return dst_file_path_name

def copy_file_sh(filename,src,dst):
	# COPY PROCESS
	# copy the files from their current location into a new folder (see Scratch file for thoughts on where new folder should be)

	# print("Found a file with the %s ending." % (user_file_ext_input))
	print("Copying file: %s" % (filename))

	shutil.copyfile(src, dst)



def scanfolder(foldername_path):
	# this function scans the parent folder and subfolders
	# it then adds them to a list so that its files can be scanned individually

	# `foldername_path` should actually be a string path to folder
	# `dirPath` - the directory path leading up to the folder's name (yet not including it), should be an absolute path I'd say
	
	# abs_cwd_file_path for foldername_path?

	dirs = os.listdir(foldername_path) # list all files of any kind (i.e. all file and folder names)
	# absPath = dirPath
	absPath = os.path.dirname(foldername_path) # returns the directory path except basename to the foldername_path

	# folder_path_list = [] # a list to hold all finalized folder paths (not folder names)

	for file in dirs:
		# new_path = os.path.join(absPath,file) # creates a path to the file/folder
		new_path = os.path.join(foldername_path,file) # creates a path to the file/folder

		if os.path.isdir(new_path): #if the file is a folder
			folder_path_list.append(new_path) # add it to the list of folders with its full path name
		else:
			continue # otherwise skip and keep going

def scanfile(foldername_path, filename, search_result_path):
	# this function scans a file to see if it matches the file type/ending specified by the user
	# os.walk(user_folder_input)?
	# os.walk(folder_path_to_be_analyzed)
	
	# `foldername_path` - the path to the folder to be analyzed
	# `search_result_path` - where you want your search results to go
	# `filename` - the name of the file in question, not necessarily a path
	
	for foldername,subfolders,filenames in os.walk(foldername_path):
		for filename in filenames:
			if file_type_regex1.search(filename):
				try:
					# SOURCE FILE
					src = find_abs_src_path(foldername_path,filename)

					# DESTINATION FILE
					dst = find_abs_dst_path(search_result_path,filename)
					
					# COPY FILE
					copy_file_sh(filename,src, dst)

				except Exception as e:
					print("There was an error and file was skipped.")
					continue
				else:
					continue



def scan_folder(foldername,regex):
	for item in foldername:
		if regex.search(item): # if the item/filename/foldername in question matches the regex target
			try:
				# SOURCE FILE
				src = find_abs_src_path(foldername,item)

				# DESTINATION FILE
				dst = find_abs_dst_path(search_result_path,item)
				
				# COPY FILE
				copy_file_sh(item,src, dst)

			except Exception as e:
				print("There was an error and file was skipped.")
				continue
			else:
				continue


def analyze_extensions(foldername_path,regex):
	for foldername,subfolders,filenames in os.walk(foldername_path):

		# analyze each folder

		for item in foldername:
			# where item is a folder
			scan_folder(item,regex)

		# analyze each subfolder
		
		for item in subfolders:
			scan_folder(item,regex)


# for foldername,subfolders,filenames in os.walk(user_folder_input):
# 	for filename in filenames:
		
# 		if file_type_regex1.search(filename):
# 			try:
				
# 				# SOURCE FILE
# 				# get the directory path leading to the file name for later source copying
# 				# we need to do this rather than using `user_folder_input` otherwise we'll miss subfolders and get errors
# 				# use `os.path.join()` to create correct path rather than string concatenation
# 				# use os.path.abspath() to make sure it's an absolute path
				
# 				src_file_path_name = os.path.abspath(os.path.join(user_folder_input,filename))

# 				# DESTINATION FILE
# 				dst_file_path_name = os.path.join(search_result_path,filename + "_" + "copy")
				
# 				# COPY PROCESS
# 				# copy the files from their current location into a new folder (see Scratch file for thoughts on where new folder should be)

# 				# print("Found a file with the %s ending." % (user_file_ext_input))
# 				print("Copying file: %s" % (filename))

# 				shutil.copyfile(src_file_path_name, dst_file_path_name)

# 			except Exception as e:
# 				# raise
# 				print("There was an error and file was skipped.")
# 				continue
# 			else:
# 				continue

#####################################
# END FILE ANALYSIS
#####################################



#####################################
# EXECUTION BLOCK
#####################################

# run an initial scan of the upper level main folder tree

# scanfolder(user_folder_input,abs_cwd_file_path)

analyze_extensions(user_folder_input,file_type_regex1)

# then scan all the sub folders

#####################################
# END EXECUTION BLOCK
#####################################

