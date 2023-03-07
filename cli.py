# Purpose:
#   Command-Line Interface for analysing a greek
#   quotation from a church father to see where
#   they quoted scripture.
# Usage:
#   To analyze a quotation from a text file:
#     python cli.py -f <filepath>
#   To analyze a quotation from an input string:
#     python cli.py -t "<input_string>"

# Import libraries
import sys
import os.path
import prob_analysis

# Get arguments
args = sys.argv

# Verify and sanitize input
if args.__len__() != 3:
  print("Usage: python cli.py -f <filepath>")
  print("OR python cli.py -t \"<quotation text>\"")
  exit(1)
elif args[1] == "-f" and not os.path.isfile(args[2]):
  print("ERROR: File does not exist")
  exit(2)
print("Yay")

# Analyze quotation
if args[1] == "-f":
  quote_filename = args[2]
# TODO: Generalize the parse and analysis functions to take any file as input
verse_analysis = prob_analysis.simple_analysis()

# Print analysis results
print(verse_analysis)