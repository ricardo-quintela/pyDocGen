# Created by Ricardo Quintela

import re

from .code_elements import find_functions, find_classes, find_indentation_level, find_strings

from dep import read_file, append_file, find_between



def google_doc_parser(path: str, md_file_path: str):
    """Parses docstrings in google pyhton format

    Args:
        path (str): the path to the file to parse
        md_file_path (str): the path to the md doc file
    """

    # read the text from the file
    try:
        text = read_file(path)

    except FileNotFoundError:
        print("ERROR: File not found")
        return


    # find all the strings
    str_ind = find_strings(text)

    # find the class indexes
    class_ind = find_classes(text)



    # ignore every occurence inside of a string
    i = 0
    while i < len(class_ind):
        for indxs in str_ind:
            if indxs[0] < class_ind[i] < indxs[1]:
                class_ind.pop(i)
                break
        else:
            i += 1



    # name of the class was already written on the file
    name_is_written = [False for i in range(len(class_ind))]

    # find the function indexes
    func_ind = find_functions(text)

    # previous function belongs to a class
    inClass = True
    prev_func_in_class = True

    
    # iterate through the functions indexes
    for i in func_ind:

        prev_func_in_class = inClass


        # check if the function belongs to a class

        # find the possible parent class
        parent_class = find_between(class_ind, i)

        # if there is a possible parent class
        if parent_class != -1:

            # check indentation level of the class and the function
            cl_ind_level = find_indentation_level(text[:parent_class + len("class")], "class")
            func_ind_level = find_indentation_level(text[:i + len("def")], "def")

            # if the indentation level of the function is superior to the one of the class by one unit then the function must be a method of that class
            if (cl_ind_level == 0 and func_ind_level > cl_ind_level) or (cl_ind_level > 0 and func_ind_level % cl_ind_level == 1):
                inClass = True
            else:
                inClass = False

        else:
            inClass = False


        # write the name of the class if it hasn't been written before
        if inClass and not name_is_written[class_ind.index(parent_class)]:

            # get the end of the name of the class index
            name_end = text.find(":", parent_class + len("class "))

            # check to see if the class has paretheses
            has_parentheses = re.search(r"\([a-zA-Z0-9\._, ]+\)", text[parent_class + len("class "): name_end])

            # generate the name of the class and the parent classes
            if has_parentheses:
                name_end = has_parentheses.start() + 1
                inheritance = has_parentheses.group()[1:-1]
                inheritance = re.sub(r", *", chr(96)*3 + ", " + chr(96)*3, inheritance)

                cl_name = text[parent_class + len("class") : parent_class + len("class") + name_end]

            else:
                inheritance = ""
                cl_name = text[parent_class + len("class") : name_end]

            


            # write the class name, description and attributes if they exist
            with open(md_file_path, "a") as file:
                append_file(file, "# The " + cl_name + " class\n  \n")


                if len(inheritance):
                    append_file(file, "**Inherits from** " + chr(96)*3 + inheritance + chr(96)*3 + "\n\n---\n  \n  ")



            name_is_written[class_ind.index(parent_class)] = True




        # write a line break if the current function no longer belongs to a class
        if prev_func_in_class and not inClass:
            with open(md_file_path, "a") as file:
                append_file(file, "\n  \n---\n  ")



        # get the signature of the function
        sig_end = text.index(":\n", i)
        signature = text[i+3 : sig_end]



        # get the name of the function
        name = signature[:signature.find("(")]


        # get the docsting indexes (start, end)
        docstring_start = text.find("\"\"\"", sig_end + 2, sig_end + 100) + 3
        
        # if docstring doesnt exist
        if docstring_start != 2:
            
            # docstring ending
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
            append_file(file, "## " + re.sub(r"_", "\\_", name) + "\n---  \n  \n**Signature:**  \n  \n>" + chr(96)*3 + re.sub(r"\n+", "", signature) + chr(96)*3 + "  \n  \n**Description:**  \n  \n>" + re.sub(r"\\n+", "  \n>", re.sub(r" {2,}", "", re.sub(r"\n+", "", description))) + "  \n  \n")
            
            # write the args if they exist
            if docstring_start != 2 and args_ind >= len("Args:\n"):
                append_file(file, "**Arguments:**  \n  \n>" + re.sub(r"\n+|\\n+", "  \n>", re.sub(r" {2,}", "", args)) + "  \n  \n")

            # write the raises if they exist
            if docstring_start != 2 and raises_ind >= len("Raises:\n"):
                append_file(file, "**Raises:**  \n  \n>" + re.sub(r" {2,}", "", raises) + "  \n  \n")
                
            # write the returns if they exist
            if docstring_start != 2 and returns_ind >= len("Returns:\n"):
                append_file(file, "**Returns:**  \n  \n>" + re.sub(r" {2,}", "", returns) + "  \n  \n")


            append_file(file, "  \n")