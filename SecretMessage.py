import os
import string
#from string import maketrans
def rename_files():
# (1) get file names in a folder
	file_list = os.listdir(r"/Users/zhihuanwilson/Downloads/prank")
	#print(file_list)
	saved_path = os.getcwd()
	print("Current Working Directory is " + saved_path)
	os.chdir(r"/Users/zhihuanwilson/Downloads/prank")
# For each file -- Rename it 
	to_remove = "0123456789"
	table = str.maketrans("", "", to_remove)
	for file_name in file_list:
		# print("Old Name - "+file_name)
		# print("New Name - "+file_name.translate(table))
		os.rename(file_name, file_name.translate(table))
		os.chdir(saved_path)


#rename_files()

def rearrage_files():
	file_list = os.listdir(r"/Users/zhihuanwilson/Downloads/prank")
	saved_path = os.getcwd()

	for i, j in zip(sorted(file_list), key=lambda x: int(x.split('.')[0]), L):
		
