# Created by Ricardo Quintela

def read_file(path: str) -> str:
    """Reads a file on the given path

    Args:
        path (str): the path to the file

    Returns:
        str: the contents of the file
    """

    with open(path, "r") as file:
        return file.read()


def new_file(path: str):
    """Creates a new empty file on the given path

    Args:
        path (str): the path where to create the file
    """

    f = open(path, "w")
    f.close()


def append_file(file, string: str):
    """Writes the given string to the file

    Args:
        file (File): the opened file where to write the string
        string (str): the string to write to the file
    """
    
    file.write(string)