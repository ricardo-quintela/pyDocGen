import os


def get_files(path: str) -> list:
    """Returns a list of the python files in the directory

    Args:
        path (str): the path to the directory to check the python files

    Returns:
        list: a list with all the python files
    """


    files = os.listdir(path)

    py_files = list()

    for file in files:
        if file[-3:] == ".py":
            py_files.append(file)

    return py_files


def get_pkg_name(path: str) -> str:
    """Gets the name of the package folder

    Args:
        path (str): the path to the package

    Returns:
        str: the package name
    """

    if path[-1] == "/" or path[-1] == "\\":
        return os.path.basename(path[:-1]).capitalize()

    return os.path.basename(path).capitalize()
    