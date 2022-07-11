import os
import sys

def read_file(path: str) -> str:
    """Reads a file on the given path

    Args:
        path (str): the path to the file

    Returns:
        str: the contents of the file
    """

    with open(path, "r") as file:
        return file.read()



def find_functions(text: str) -> list:
    """Finds the indexes of all the definitions on the code

    Args:
        text (str): the text to find the definitions on

    Returns:
        list: the indexes of the functions
    """

    func_ind = list()

    slice_ind = 0

    while (ind := text.find("def ", slice_ind)) != -1:
        func_ind.append(ind+1)
        slice_ind = ind+3

    return func_ind


def google_doc_parser(path: str):

    try:
        text = read_file(path)

    except FileNotFoundError:
        print("ERROR: File not found")

    # create a directory
    try:
        os.mkdir(os.path.dirname(path).replace("/", "\\") + "\\docs")

    except FileExistsError:
        pass

    md_file_path = os.path.dirname(path).replace("/", "\\") + "\\docs\\" + os.path.basename(path)[:os.path.basename(path).find(".")] + ".md"

    
    # create an empty file
    f = open(md_file_path, "w")
    f.close()


    # find the function indexes
    func_ind = find_functions(text)

    
    # iterate through the functions indexes
    for i in func_ind:

        # get the signature of the function
        sig_end = text.index(":\n", i)

        signature = text[i+4 : sig_end]


        # get the name of the function
        name = signature[0:signature.find("(")]


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
        if args_ind == len("Args:\n") - 1:

            # arguments and returns dont exist
            if returns_ind == len("Returns:\n") - 1:
                description = text[docstring_start: docstring_end]
            
            # arguments dont exist but returns does
            else:
                description = text[docstring_start: returns_ind - len("Returns:\n")]

        # arguments exists
        else:
            description = text[docstring_start: args_ind - len("Args:\n")]


        # get the arguments

        # returns exists
        if returns_ind != len("Returns:\n") - 1:
            args = text[args_ind: returns_ind - len("Returns:\n")]

        # raises exists but returns doesnt
        elif raises_ind != len("Raises:\n") - 1:
            args = text[args_ind : raises_ind - len("Raises:\n")]
        
        # returns and raises dont exist
        else:
            args = text[args_ind : docstring_end]


        # get the returns

        # raises exists
        if raises_ind != len("Raises:\n") - 1:
            returns = text[returns_ind: raises_ind - len("Raises:\n")]
        
        # returns doesnt exist
        else:
            returns = text[returns_ind : docstring_end]


        # get the raises
        raises =  text[raises_ind : docstring_end]


        with open(md_file_path, "a") as file:

            file.write("### " + name + "  \n  \n**Signature:**  \n  \n" + chr(96)*3 + signature.replace("  ", "") + chr(96)*3 + "  \n  \n**Description:**  \n  \n" + description.replace("  ", "") + "  \n  \n")
            
            if args_ind != len("Args:\n") - 1:
                file.write("**Arguments:**  \n  \n" + args.replace("  ", "") + "  \n  \n")

            if returns_ind != len("Returns:\n") - 1:
                file.write("**Returns:**  \n  \n" + returns.replace("  ", "") + "  \n  \n")

            if raises_ind != len("Raises:\n") - 1:
                file.write("**Raises:**  \n  \n" + raises.replace("  ", "") + "  \n  \n")

            file.write("  \n")




def main(argv: tuple) -> None:
    """Main function of the code

    Args:
        argv (tuple): the command line args
    """

    if len(argv) == 0:
        print("Please input a file path or --help to show a help message")
        return

    elif argv[1] == "--help":
        print("HELP MESSAGE HERE")
        return

    elif argv[1] == "-g":
        doctype = 1

    else:
        print("Please input a file path or --help to show a help message")
        return

    if doctype == 1:
        google_doc_parser(argv[2])

    
    # start the parsing

if __name__ == "__main__":
    main(sys.argv)