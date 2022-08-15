import os

def find_between(arr: list, num: int) -> int:
    """Checks if a given number can be put between two others in the given array

    Args:
        arr (list): the list of numbers
        num (int): the number to compare

    Returns:
        int: the number right before the one given (num) or -1 if it fails
    """
    if len(arr) == 0:
        return -1

    if len(arr) < 2:
        return arr[0] if num > arr[0] else -1

    for i in range(len(arr) - 1):
        if arr[i] < num < arr[i+1]:
            return arr[i]

    if arr[-1] < num:
        return arr[-1]
        

def get_mdpath(path: str) -> str:
    """Parses the given file path and returns a path to the md file to create and write

    Args:
        path (str): the python file path

    Returns:
        str: the path to the md file
    """
    # relative path
    if os.path.dirname(path) == "":

        # create a directory
        try:
            os.mkdir("docs")

        except FileExistsError:
            pass

        md_file_path = "docs\\" + os.path.basename(path)[:os.path.basename(path).find(".")] + ".md"

    # absolute path
    else:
        # create a directory
        try:
            os.mkdir(os.path.dirname(path) + "\\docs")

        except FileExistsError:
            pass

        md_file_path = os.path.dirname(path) + "\\docs\\" + os.path.basename(path)[:os.path.basename(path).find(".")] + ".md"


    return md_file_path