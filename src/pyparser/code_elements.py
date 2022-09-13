# Created by Ricardo Quintela

import re

def find_functions(text: str) -> list:
    """Finds the indexes of all the definitions on the code

    Args:
        text (str): the text to find the definitions on

    Returns:
        list: the indexes of the functions
    """

    func_ind = list()

    matches = re.finditer(r"[\t ]*def [a-zA-Z0-9_]+\(+[\S\n\t\v ]*?\)+:", text)

    for match in matches:
        func_ind.append(match.start() + len(re.findall(r"[\t ]*def", match.group(0))[0]) - len("def") + 1)

    return func_ind


def find_classes(text: str) -> list:
    """Finds the indexes of all the classes on the code

    Args:
        text (str): the text to find the classes on

    Returns:
        list: the indexes of all the classes in the code
    """
    class_ind = list()

    matches = re.finditer(r"[\t ]*class [a-zA-Z0-9_]+\(*[\S\n\t\v ]*?\)*:", text)

    for match in matches:
        class_ind.append(match.start() + len(re.findall(r"[\t ]*class", match.group(0))[0]) - len("class") + 1)

    return class_ind


def find_indentation_level(string: str, keyword: str) -> int:
    """Finds the indentation level of a given string considering that
     the string has a python keyword on it

    Args:
        string (str): the string to find the identation level
        keyword (str): the keyword to start the search

    Returns:
        int: the number of spaces or tabs before the first keyword or -1 if it fails
    """

    matches = re.findall(r"[\t ]*" + keyword, string)

    if len(matches) < 1:
        return -1

    return len(matches[-1].replace(keyword, ""))


def find_strings(text: str) -> list:
    """Finds all the strings in the code

    Args:
        text (str): the text to find the strings on

    Returns:
        list: the start and end indexes of all the strings in the code
    """
    str_ind = list()

    matches = re.finditer(r"\"[\S\n\t\v ]*?\"", text)

    for match in matches:
        str_ind.append((match.start(), match.end()))

    
    return str_ind