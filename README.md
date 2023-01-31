# pyDocGen
 Markdown documentation generator for python

## Current support

* Scanning of entire packages for pyhton files
* Google style docstrings

# How to use

```
usage: pydocgen.py [-h] [-p] -g path

Create documentation from docstrings for python files

positional arguments:
  path           path to the file or folder

optional arguments:
  -h, --help     show this help message and exit
  -p, --package  parse all .py files in a package
  -g, --google   parse using google style docstrings
```


# Requirements

[Python 3.8](https://www.python.org/downloads/release/python-380/) or above  
Regular Expressions package (usualy comes with standard library)
