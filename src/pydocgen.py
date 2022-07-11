# Created by Ricardo Quintela

import sys

from dep import read_file

from pyparser import google_doc_parser


def main(argv: tuple) -> None:
    """Main function of the code

    Args:
        argv (tuple): the command line args
    """

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

    # parsing
    if doctype == 1:
        google_doc_parser(argv[2])


if __name__ == "__main__":
    main(sys.argv)