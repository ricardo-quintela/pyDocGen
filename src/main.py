import sys

from pyparser import google_doc_parser

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