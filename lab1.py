import os
from pathlib import Path
import shutil

def directoryInput():
	'''This function prompts the user to input a directory. If the directory is not found, it will prompt the user.'''
	invalid_input = True
	while(invalid_input):
		str_input = input("")
		if(len(str_input) != 0):
			p = Path(str_input)
			if(p.exists()):
				found_files = searchInput(p)
				if (len(found_files) != 0):
					invalid_input = False
					actionInput(found_files)
			else:
				print("ERROR")
		else:
			print("ERROR")

def searchInput(p:Path)->[Path]:
	'''This function gives the user the option to find a specific file (n), find files with a specific extention (e), or find files greater
	than a given size (s).'''

	file_list = findFiles(p)
	invalid_input = True
	while (invalid_input):
		str_input = input("")
		if (len(str_input) != 0): 
			choice = str_input[0].lower()
			arg = str_input[2:]
			found_list = []

			if (choice == 'n'):
				found_list = findSpecificFile(file_list,arg)
			elif (choice == 'e'):
				found_list = findFileWithExtension(file_list,arg)
			elif (choice == 's'):
				if (arg.isdigit()):
					found_list = findFileBySize(file_list,eval(arg))		
			if (len(found_list) != 0):
				return found_list
		else:
			print("ERROR")
	return[]

def findFiles(path:Path)->[Path]:
	lst = []
	for p in path.iterdir():
		try:
			if(p.is_file()):
				lst.append(p)
			elif(p.is_dir()):
				lst.extend(findFiles(p))

		except:
			continue
	return lst

def findSpecificFile(path_list:[Path], file_name:str)->[Path]:
	lst = []
	for p in path_list:
		if (p.name == file_name):
			lst.append(p)
	return lst

def findFileWithExtension(path_list:[Path], ext:str)->[Path]:
	lst = []
	for p in path_list:
		if(p.suffix == ext or p.suffix == '.' + ext):
			lst.append(p)
	return lst

def findFileBySize(path_list:[Path], size:int)->[Path]:
	lst = []
	for p in path_list:
		if(p.stat().st_size > size):
			lst.append(p)
	return lst

def actionInput(path_list:[Path]):
	'''This function gives the user the option to print the path of the given file (p), print the first line of the contents of a given file (f),
	duplicate the file by adding ".dup" to the end of the file name (d), or update the access/modified time of the file (t)'''
	invalid_input = True

	while(invalid_input):
		str_input = input("")
		if(len(str_input) != 0):
			choice = str_input[0].lower()

			if (choice == 'p'):
				invalid_input = False
				printFilePath(path_list)
			elif (choice == 'f'):
				invalid_input = False
				printFileContents(path_list)
			elif (choice == 'd'):
				invalid_input = False
				duplicateFile(path_list)
			elif (choice == 't'):
				invalid_input = False 
				updateFileTime(path_list)
			else:
				print("ERROR")
		else:
			print("ERROR")

def printFilePath(path_list:[Path]):
	'''This function prints the path of a file'''
	for path in path_list:
		print(path)

def printFileContents(path_list:[Path]):
	'''This function prints the first line of the content of each file'''
	for path in path_list:
		try:
			file = path.open()
			print(path)
			print(file.readline())
			file.close()
		except:
			print("ERROR")

def duplicateFile(path_list:[Path]):
	'''This function creates a copy of a file, adds ".dup" to the end of the filename, and saves it in the same directory as the
	original file'''
	for path in path_list:
		shutil.copy2(str(path),str(path)+".dup")

def updateFileTime(path_list:[Path]):
	'''This function updates the access/modified time of the given file'''
	for path in path_list:
		os.utime(str(path), None)

if __name__ == '__main__':
	directoryInput()
