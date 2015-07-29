#! /usr/bin/python
"""
This script accepts a string with the following syntax:

Get the list of classes that a PHP class depends on.

Generate PHP code that 

  defines the fields with corresponding
names ( same name as the class name but with the first letter
converted to lower case ).

  defines the constructor.
  
Print out the code to the console.

"""
import sys
from generator.generator import Generator
from pyperclip.pyperclip import copy

def main():
    """
    Parse arguments from command line
    """
    argv = sys.argv
    length = len(argv)
    if length != 2:
        print_help()
        exit()
    dependent_list_string = sys.argv[1]
    statement = Generator.generate_statements(dependent_list_string)
    copy(statement)
    print statement

def print_help():
    """
    Prints the help string for this script
    """
    print "php-di-gen.py <dependent class list string>"

main()
