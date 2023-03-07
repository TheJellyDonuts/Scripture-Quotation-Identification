# Purpose:
#   Command-Line Interface for analysing a greek
#   quotation from a church father to see where
#   they quoted scripture.
# Usage:
#   To analyze a quotation from a text file:
#     python cli.py -f <filename>
#   To analyze a quotation from an input string:
#     python cli.py -t "<input_string>"

# Import libraries
import sys
import os.path

# Get arguments
args = sys.argv

# Verify and sanitize input
if args.__len__() != 4:
  print("Usage: python cli.py -f <filename>")
  print("OR python cli.py -t \"<quotation text>\"")
  exit()
elif args[2] == "-f" and not os.path.isfile(args[3]):
  print("ERROR: File does not exist")
  exit()
print("Yay")
