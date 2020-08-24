# importing the required modules
import os
import shutil
import time

def remove_folder(path):

	# removing the folder
	if not shutil.rmtree(path):

		# success message
		print(f"{path} is removed successfully")

	else:

		# failure message
		print(f"Unable to delete the {path}")


def remove_file(path):

	# removing the file
	if not os.remove(path):

		# success message
		print(f"{path} is removed successfully")

	else:

		# failure message
		print(f"Unable to delete the {path}")


def get_file_or_folder_age(path):

	# getting ctime of the file/folder
	# time will be in seconds
	ctime = os.stat(path).st_ctime

	# returning the time
	return ctime

def clean():
	# initializing the count
	deleted_folders_count = 0
	deleted_files_count = 0

	# specify the path
	path = "C:\\Users\\matpr\\Desktop\\Flask-YouTube-master\\media"

	# specify the seconds
	seconds = 10800

	# converting seconds to seconds
	# time.time() returns current time in seconds
	seconds = time.time() - seconds

	# checking whether the file is present in path or not
	if os.path.exists(path):

		# iterating over each and every folder and file in the path
		for root_folder, folders, files in os.walk(path):

			# comparing the seconds
			if seconds >= get_file_or_folder_age(root_folder):

				# removing the folder
				remove_folder(root_folder)
				deleted_folders_count += 1 # incrementing count

				# breaking after removing the root_folder
				break

			else:

				# checking folder from the root_folder
				for folder in folders:

					# folder path
					folder_path = os.path.join(root_folder, folder)

					# comparing with the seconds
					if seconds >= get_file_or_folder_age(folder_path):

						# invoking the remove_folder function
						remove_folder(folder_path)
						deleted_folders_count += 1 # incrementing count


				# checking the current directory files
				for file in files:

					# file path
					file_path = os.path.join(root_folder, file)

					# comparing the seconds
					if seconds >= get_file_or_folder_age(file_path):

						# invoking the remove_file function
						remove_file(file_path)
						deleted_files_count += 1 # incrementing count

		else:

			# if the path is not a directory
			# comparing with the seconds
			if seconds >= get_file_or_folder_age(path):

				# invoking the file
				remove_file(path)
				deleted_files_count += 1 # incrementing count

	else:

		# file/folder is not found
		print(f'"{path}" is not found')

	print(f"Total folders deleted: {deleted_folders_count}")
	print(f"Total files deleted: {deleted_files_count}")
