import os, shutil
from pathlib import Path

def rename_folders():
	p = Path('.')
	cwd = os.getcwd()

	for folder in p.iterdir():
		if folder.is_dir():
			rename_files(folder, cwd)

def format_folder_name(folder_name):
	new_name = folder_name[0:3] + "_" + folder_name[6:]
	return new_name

def rename_files(folder, dest):
	file_name = format_folder_name(str(folder))
	count = 1
	for file in folder.iterdir():
		new_file_name = file_name + "_" + str(count)
		new_file_name = new_file_name.replace(" ", "_")
		new_file_name = new_file_name + (".jpg")

		file.rename(new_file_name)
		#move_file(file, dest)

		count += 1
	folder.rmdir()

def move_file(file, dest):
	move(file, dest)

if __name__ == "__main__":
	rename_folders()