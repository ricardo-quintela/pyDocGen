# Created by Ricardo Quintela

import sys
import argparse

from dep import get_mdpath, new_file
from pkg_handeler import get_files, get_pkg_name

from pyparser import google_doc_parser


def main(argv: tuple) -> None:
    """Main function of the code

    Args:
        argv (tuple): the command line args
    """

    # parse the arguments
    argparser = argparse.ArgumentParser(description="Create documentation from docstrings for python files")

    argparser.add_argument(
        "-p", "--package",
        help="parse all .py files in a package",
        action="store_true"
    )

    argparser.add_argument(
        "path",
        help="path to the file or folder",
        type=str
    )

    format_group = argparser.add_mutually_exclusive_group(required=True)
    format_group.add_argument(
        "-g", "--google",
        help="parse using google style docstrings",
        action="store_true",
    )

    args = argparser.parse_args()


    # package handling
    if args.package:

        # get the files in the given folder
        py_files = get_files(args.path)

        # get the package name and the path to the md file
        pkg_name = get_pkg_name(args.path)
        file_path = get_mdpath(args.path + "\\" + pkg_name + ".")

        # create a new file and write the name of the package on the top
        with open(file_path, "w") as file:
            file.write("# The " + pkg_name + " package\n\n")


        for path in py_files:

            # parsing in google format doc
            if args.google:
                google_doc_parser(args.path + "\\" + path, file_path)

            # make a separator
            with open(file_path, "a") as file:
                file.write("\n\n  ---\n\n  ")

        return


    # create a new file and get the md file path
    file_path = get_mdpath(args.path)
    new_file(file_path)

    # parsing
    if args.google:
        google_doc_parser(args.path, file_path)


if __name__ == "__main__":
    main(sys.argv)