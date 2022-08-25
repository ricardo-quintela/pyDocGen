# Created by Ricardo Quintela

import sys

from dep import read_file, get_mdpath, new_file
from pkg_handeler import get_files, get_pkg_name

from pyparser import google_doc_parser


def main(argv: tuple) -> None:
    """Main function of the code

    Args:
        argv (tuple): the command line args
    """

    # package scan
    if len(argv) > 2 and "--" in argv[2]:

        # correct syntax
        if "--pkg" in argv[2]:
            isPackage = True
        
        # incorrect syntax
        else:
            print("Please input a file path or --help to show a help message")
            return
    else:
        isPackage = False

    # no arguments
    if len(argv) == 1:
        print("Please input a file path or --help to show a help message")
        return

    # help argument
    elif argv[1] == "--help":
        print(read_file("resources/help.txt"))
        return

    # google style doc
    elif argv[1] == "-g":
        doctype = 1

    # wrong parameters
    else:
        print("Please input a file path or --help to show a help message")
        return


    # package handling
    if isPackage:

        # get the files in the given folder
        py_files = get_files(argv[3])

        # get the package name and the path to the md file
        pkg_name = get_pkg_name(argv[3])
        file_path = get_mdpath(argv[3] + "\\" + pkg_name + ".")

        # create a new file and write the name of the package on the top
        with open(file_path, "w") as file:
            file.write("# The " + pkg_name + " package\n\n")


        for path in py_files:

            # parsing in google format doc
            if doctype == 1:
                google_doc_parser(argv[3] + "\\" + path, file_path)

            # make a separator
            with open(file_path, "a") as file:
                file.write("\n\n  ---\n\n  ")

        return


    # create a new file and get the md file path
    file_path = get_mdpath(argv[2])
    new_file(file_path)

    # parsing
    if doctype == 1:
        google_doc_parser(argv[2], file_path)


if __name__ == "__main__":
    main(sys.argv)