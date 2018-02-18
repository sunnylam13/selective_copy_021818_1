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

# a list of all files to be analyzed
file_path_list = [] # a list to hold all finalized folder paths (not folder names)


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

def find_abs_dst_path(path,filename,regex):
	# dst_file_path_name = os.path.join(search_result_path,filename + "_" + "copy")
	dst_file_path_name = os.path.join(path,file_type_regex1.sub("_copy" + user_file_ext_input,filename)) # use regex substitution to change the file name so that shutil.copyfile() will work as it won't work if the names are identical for some reason?

	return dst_file_path_name

def copy_file_sh(filename,src,dst):
	# COPY PROCESS
	# copy the files from their current location into a new folder (see Scratch file for thoughts on where new folder should be)

	# print("Found a file with the %s ending." % (user_file_ext_input))
	print("Copying file: %s" % (filename))

	shutil.copyfile(src, dst)


def scanFolder(foldername_path):
	# this function scans the parent folder and subfolders
	# it then adds them to a list so that its files can be scanned individually

	# `foldername_path` should actually be a string path to folder
	# `dirPath` - the directory path leading up to the folder's name (yet not including it), should be an absolute path I'd say
	
	# abs_cwd_file_path for foldername_path?

	# as we get deeper and deeper into subfolders it should add onto the folder's path string that we pass to it so accuracy should be maintained

	dirs = os.listdir(foldername_path) # list all files of any kind (i.e. all file and folder names)
	# absPath = dirPath
	# absPath = os.path.dirname(foldername_path) # returns the directory path except basename to the foldername_path

	# folder_path_list = [] # a list to hold all finalized folder paths (not folder names)

	for file in dirs:
		# new_path = os.path.join(absPath,file) # creates a path to the file/folder
		new_path = os.path.join(foldername_path,file) # creates a path to the file/folder

		if os.path.isdir(new_path): #if the file is a folder
			folder_path_list.append(new_path) # add it to the list of folders with its full path name
		else:
			continue # otherwise skip and keep going

def scanFile(foldername_path,regex):
	# the file scanner that gets all of the files and pushes them into a list after we get the full string path to it
	
	dirs = os.listdir(foldername_path) # list all files of any kind (i.e. all file and folder names)

	for file in dirs:
		# new_path = os.path.join(absPath,file) # creates a path to the file/folder
		new_path = os.path.join(foldername_path,file) # creates a path to the file/folder

		if os.path.isfile(new_path) and regex.search(file): #if the file is a folder AND has regex match
			file_path_list.append(new_path) # add it to the list of folders with its full path name
		else:
			continue # otherwise skip and keep going

def analyzeAllFiles ():
	# run an initial scan of the upper level main folder tree
	# find subfolders
	# find matching files
	scanFolder(user_folder_input)
	scanFile(user_folder_input,file_type_regex1)

	# then scan all the sub folders by cycling through folder_path_list until no more subfolders are added
	# this should keep going until no more subfolders are analyzed
	# then scan all the files by cycling through folder_path_list until no more subfolders are added/left
	for subfolder in folder_path_list:
		scanFolder(subfolder)
		scanFile(subfolder,file_type_regex1)

	# print(folder_path_list)
	# print(file_path_list)

	# then go through the file list that meets criteria and copy
	for match_file in file_path_list:
		# match_file - already a string file path if done right, aka file source
		get_fileBaseName = os.path.basename(match_file) # this should be the name of the file only with the rest of the path to the left stripped away
		src_file = match_file
		dst_file = find_abs_dst_path(search_result_path,get_fileBaseName,file_type_regex1)
		copy_file_sh(get_fileBaseName,src_file,dst_file)

#####################################
# END FILE ANALYSIS
#####################################



#####################################
# EXECUTION BLOCK
#####################################

analyzeAllFiles()

print("The destination folder is:  %s" % (search_result_path))

#####################################
# END EXECUTION BLOCK
#####################################

