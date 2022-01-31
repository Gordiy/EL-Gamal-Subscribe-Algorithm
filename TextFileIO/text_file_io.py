"""Working with file."""
from .constants import path_to_file_read, path_to_file_write


class TextFileIO:
    """Definition methods that read and write data from/to file."""
    @staticmethod
    def file_read():
        file = open(f"{path_to_file_read}.txt", 'r')
        return file.read()

    @staticmethod
    def file_write(data, data_and_time):
        """Write data to file or append data to exist file."""
        file = open(f"{path_to_file_write}{data_and_time}.txt", 'a')
        file.write(f"{data}\n")
        file.close()
