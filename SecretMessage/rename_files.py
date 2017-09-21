import os

#this is my first python function
def rename_files():

	# 1 get file names from a folder
	file_list = os.listdir("./prank")
	print(file_list)

	# 2 rename files without the numbers

rename_files()
