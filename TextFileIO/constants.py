"""Constans needed for package that write and read data to/from file."""
import os


filename_read = 'readfile'
filename_write = 'writefile_'

path_to_file_read = f"{os.getcwd()}/temp/read/{filename_read}"
path_to_file_write = f"{os.getcwd()}/temp/write/{filename_write}"
