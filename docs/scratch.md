# Scratch File

## Sunday, February 18, 2018 1:35 PM

We're going to just automatically create the new folder with the copied files in the cwd or "current working directory".

It would be possible in the future to write the program to output to a user specified directory.

Or we could make it default to the master level parent like `C:\\` or `/` or the user's main parent (`~/`).

In the case of using any destination directory we should print the name of the directory it will be stored in at the end of the program.

## Sunday, February 18, 2018 4:10 PM

It may be better to do as I've done in the past and create the filename path strings and push to a list or a dict before doing the copy process.

In this case each filename has a unique source location path string and a destination location path string so a dict may be more useful to use instead.

## Sunday, February 18, 2018 4:32 PM

What we need is to get the current working directory and then add the subfolder name to the absolute path of the cwd as we go deeper and deeper into a folder... in order to get the right path.

## Sunday, February 18, 2018 5:14 PM

KEY POINT:  Apparently if you use os.path.join() with only a folder and filename in the os.walk() loops, you don't need to find the file paths yourself.  

The system will construct everything for you.

Since we're only copying files, and not altering file names or listing file contents by their full path, getting the full directory path to a file or folder may not be necessary...

Never mind, you definitely need them.