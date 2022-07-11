# Created by Ricardo Quintela

import os
import re

from .code_elements import find_functions

from dep import read_file, new_file, append_file



def google_doc_parser(path: str):
    """Parses docstrings in google pyhton format

    Args:
        path (str): the path to the file to parse
    """

    try:
        text = read_file(path)

    except FileNotFoundError:
        print("ERROR: File not found")

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


    
    # create an empty file
    f = new_file(md_file_path)


    # find the function indexes
    func_ind = find_functions(text)

    
    # iterate through the functions indexes
    for i in func_ind:

        # get the signature of the function
        sig_end = text.index(":\n", i)
        signature = text[i+3 : sig_end]



        # get the name of the function
        name = signature[:signature.find("(")]



        # get the docsting indexes (start, end)
        docstring_start = text.find("\"\"\"", sig_end + 2, sig_end + 100) + 3
        
        # if docstring doesnt exist
        if docstring_start == 2:
            continue
            
        docstring_end = text.find("\"\"\"", docstring_start)



        # arguments start index
        args_ind = text.find("Args:\n", docstring_start, docstring_end) + len("Args:\n")



        # returns start index
        returns_ind = text.find("Returns:\n", docstring_start, docstring_end) + len("Returns:\n")



        # raises start index
        raises_ind = text.find("Raises:\n", docstring_start, docstring_end) + len("Raises:\n")
        


        # make a description
        if args_ind < len("Args:\n") and raises_ind < len("Raises:\n") and returns_ind < len("Returns:\n"):
                description = text[docstring_start: docstring_end]
            
        # arguments dont exist but raises does
        elif args_ind < len("Args:\n") and raises_ind >= len("Raises:\n"):
            description = text[docstring_start: raises_ind - len("Raises:\n")]

        # arguments and raises dont exist but returns does
        elif args_ind < len("Args:\n") and raises_ind < len("Raises:\n") and returns_ind >= len("Returns:\n"):
            description = text[docstring_start: returns_ind - len("Returns:\n")]

        # arguments exists
        else:
            description = text[docstring_start: args_ind - len("Args:\n")]




        # get the arguments

        # raises exists
        if raises_ind >= len("Raises:\n"):
            args = text[args_ind: raises_ind - len("Raises:\n")]

        # raises exists but returns doesnt
        elif returns_ind >= len("Returns:\n"):
            args = text[args_ind : returns_ind - len("Returns:\n")]
        
        # returns and raises dont exist
        else:
            args = text[args_ind : docstring_end]



        # place backticks surrounding the var name
        var_indexes = re.finditer(r"[a-zA-Z0-9_]+: |[a-zA-Z0-9_]+ \(", args)

        for var in var_indexes:
            args = args.replace(var.group(0), chr(96)*3 + var.group(0)[:-2] + chr(96)*3 + var.group(0)[-2:])

        # place backticks surrounding the var name
        type_indexes = re.finditer(r" \([a-zA-Z0-9_]+\):", args)

        for var in type_indexes:
            args = args.replace(var.group(0), " (" + chr(96)*3 + var.group(0)[2:-2] + chr(96)*3 + "):")
        



        # get the returns

        # returns exists
        if returns_ind >= len("Returns:\n"):
            raises = text[raises_ind: returns_ind - len("Returns:\n")]
        
        # returns doesnt exist
        else:
            raises = text[raises_ind: docstring_end]



        # get the returns
        returns =  text[returns_ind : docstring_end]



        # write everything to the file
        with open(md_file_path, "a") as file:

            # write the name and the description
            append_file(file, "### " + re.sub("_", "\\_", name) + "  \n  \n**Signature:**  \n  \n>" + chr(96)*3 + re.sub(r"\n+", "", signature) + chr(96)*3 + "  \n  \n**Description:**  \n  \n>" + re.sub(r"\\n+", "  \n>", re.sub(r" {2,}", "", re.sub(r"\n+", "", description))) + "  \n  \n")
            
            # write the args if they exist
            if args_ind >= len("Args:\n"):
                append_file(file, "**Arguments:**  \n  \n>" + re.sub(r"\n+|\\n+", "  \n>", re.sub(r" {2,}", "", args)) + "  \n  \n")

            # write the raises if they exist
            if raises_ind >= len("Raises:\n"):
                append_file(file, "**Raises:**  \n  \n>" + raises.replace("  ", "") + "  \n  \n")
                
            # write the returns if they exist
            if returns_ind >= len("Returns:\n"):
                append_file(file, "**Returns:**  \n  \n>" + returns.replace("  ", "") + "  \n  \n")


            append_file(file, "  \n")