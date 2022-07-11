import re

def find_functions(text: str) -> list:
    """Finds the indexes of all the definitions on the code

    Args:
        text (str): the text to find the definitions on

    Returns:
        list: the indexes of the functions
    """

    func_ind = list()

    matches = re.finditer("\s+def ", text)

    for match in matches:
        func_ind.append(match.end() - len("def"))

    return func_ind