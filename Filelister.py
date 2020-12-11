#!python3
#file lister with Size
import logging, os,pprint
from pathlib import Path

#start dubugging
logging.basicConfig(level = logging.DEBUG, format = ' %(asctime)s - %(levelname)s - %(message)s ')

#current working directory
logging.debug(Path.cwd())

class Filelister:
	"""main class handle most of the programme"""

	def __init__(self, file, dirs):
		"""intialize all the variable need for the programme"""
		self.file = file
		self.dirs = dirs
		self.mytxt = open('mytxt.txt', 'a')

	def lister(self):
		"""list all folders and files and their sizes"""

		#this loop through all the directories and its files
		for folderName, subfolders, filenames in os.walk(self.dirs):
			logging.debug(folderName)#write folder name and its size
			self.mytxt.write(f"{folderName} - {self._get_size('GB', folderName)} \n ")
			#write subfolders of Folder and thier sizes
			self.mytxt.write(f"folders: \n")
			for subfolder in subfolders:
				self.mytxt.write(f" 	{subfolder}\n")

			#write files in Folder and thier sizes
			self.mytxt.write(f"\n files: \n")
			for filename in filenames:
				self.mytxt.write(f"		{filename} - {self._get_size('MB', folderName, filename)}\n ")
			self.mytxt.write('\n')

		self.mytxt.close()
	
	def _get_size(self, md, path1, path2 = ''):
		totalsize = 0
		if path2 == '':
			for folderName, subfolders, filenames in os.walk(path1):
				for filename in filenames:
					fp = os.path.join(folderName, filename)
					totalsize += os.path.getsize(fp)
		elif path2 != '':
			fp = os.path.join(path1, path2)
			totalsize += os.path.getsize(fp)

		if md == "GB":
			return str((totalsize/(1024*1024*1024)))[:5] + " GB"
		elif md == "MB":
			return str((totalsize/(1024*1024)))[:5] + " MB"

#Name the file path from which the file should be listed
lits = ["F:\\Dev", "D:\\devashish\\torrent\\watching", "G:\\Dev"]
for lis in lits:
	file = Filelister('mytxt.txt', lis)
	file.lister()

input("============The End (T-T)============")
