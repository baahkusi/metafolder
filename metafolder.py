""" Metafolder is a simple python utility
---

@author: sbk

1. It provides functionality that lets one group a large collection of files.
2. It automatically detects all file properties present in a folder.
3. The grouping properties are then selected.
4. Files are then arranged into folders named by properties.

"""
from pathlib import Path

class MetaFolder:
	""" This is the metafolder class 
		
		Basically provides file grouping functionalities
	"""
	# _wkdir is meant to be a private variable (Path object) that stores the working directory of the class
	# _exts is meant to be a private variable that stores a set of current file properties
	def __init__(self,wkdir="."):
		""" Initialize MetaFolder """
		self._wkdir = Path(wkdir)
		if self._wkdir.exists():
			self._exts = self.collect_exts()
		else:
			raise Exception("No such file or directory exists")

	def __str__(self):
		""" This method returns a string representation of the absolute path to the working directory """
		return str(self._wkdir.resolve())

	def collect_exts(self):
		""" Collects extensions of all the files and returns a set object """

		# Collect all avialable file extensions
			# Go through wkdir, collect a list of all the names of the files
			# Extract file extensions into another list and return a set
		exts  = [file.suffix.strip('.') for file in self._wkdir.iterdir() if file.is_file()]
		return set(exts)

	def fold(self):
		""" This method groups files in their respective folders according to their extensions """

		# Create folders using a prefix and names in _exts, pass over already existing folders
		for ext in self._exts:
			self._wkdir.joinpath('metafolder_'+ext).mkdir(exist_ok=True)
		# move files into their respective folders
		for file in self._wkdir.iterdir():
			if not file.is_file():
				pass
			else:
				try:
					file.rename(str(file.parent)+'/metafolder_'+file.suffix.strip('.')+'/'+file.name)
				except FileNotFoundError:
					pass