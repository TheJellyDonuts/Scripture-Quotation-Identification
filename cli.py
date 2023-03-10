'''
Kobe Couvion
03-07-2023

~ ~ QUOTATION IDENTIFICATION CLI ~ ~

Purpose:
  Creates a command-line interface for analyzing a
  church father greek quotation from either a text file
  or raw (greek) text input. 
Usage:
  To analyze a quotation from an input string:
    python cli.py -t "<input_string>"
  To analyze a quotation from a text file:
    python cli.py -f <filepath>
  To analyze quotations from multiple text files
  (i.e. a batch analysis):
    python cli.py -b <filepath> <filepath> ...
Dev Notes:
  The results are now generated by a function rather
  than just executing the file, which allows us to
  call the function in other places to accomplish
  those same results.
'''

# Import libraries
import sys
import os.path
import prob_data
# import prob_analysis
from lazy_import import lazy_module
# Import the module lazily
prob_analysis = lazy_module('prob_analysis')

# Create a temp file for greek input text
def read_in_greek(original_greek: str):
  temp_file = open("original_greek.txt", "w")
  temp_file.write(original_greek)
  temp_file.close();
  return temp_file.name()

# Sanitize input file/text BEFORE ANYTHING ELSE
def sanitize_input(input: str, is_file: bool):
  extension: str = os.path.splitext(input)[1]
  if is_file:
    # Check that file exists and is not harmful
    if not os.path.isfile(input):
      raise Exception("File does not exist")
    elif extension != ".txt":
      raise Exception("Only .txt files are acceptable.")
    else:
      # TODO: Handle malicious file catching
      return
  else:
    # TODO: Handle malicious text catching
    return
  
# Do the probability analysis
def analyze_data(filename: str):
  # Parse the input and generate probabilit data
  prob_data.synthesize(filename)
  # Analyze the probability data against the Greek New Testament
  output_list = prob_analysis.simple_analysis(True)
  return output_list

# Dump the analysis output into a text file
def generate_output(input_filename: str, output_list: list):
  # Create output file
  output_filename: str = ""
  if input_filename == "original_greek.txt":
    output_filename = "quotation_analysis.txt"
  else:
    output_filename = os.path.splitext(input_filename)[0] + "_analysis.txt"
  output_file = open(output_filename, "w")
  
  # Write analysis results to output file
  # TODO: Update this write loop to collect up to top three verses for each clause and display them
  #versecount: int = 0
  #for i in range(clause_list.__len__()):
  #  # Write the next clause
  #  output_file.write(clause_list[i] + "\n")
  #  # Write the verse that best matches it
  #  output_file.write(output_list[i] + "\n\n")

  # Close file and inform user
  print("Quotation analyzed.")
  print("Analysis written to " + output_filename + ".")
  exit(0)
    
# Run the interface through the web app
def web_process(input: str):
  sanitize_input(input)
  f = read_in_greek(input)
  o = analyze_data(f)
  # Cleanup
  os.remove("original_greek.txt")
  return o  

# Run the interface through the command line
def cli_process():
  # Get arguments
  args = sys.argv

  # Verify CLI usage
  l = args.__len__()
  if l < 3 or (args[1] == "-f" and l != 3) or (args[1] == "-t" and l != 3):
    print("Usage: python cli.py -f <filepath>")
    print("OR     python cli.py -t \"<quotation text>\"")
    print("OR     python cli.py -b <filepath> <filepath> ...")
    exit(1)
  
  # Sanitize input and grab filename(s)
  input_filename = []
  if args[1] == "-f":
    sanitize_input(args[2], True)
    input_filename.append(args[2])
  elif args[1] == "-t":
    sanitize_input(args[2], False)
    input_filename.append(read_in_greek(args[2]))
  elif args[1] == "-b":
    for i in range(2, args.__len__()):
      sanitize_input(args[i], True)
      input_filename.append(args[i])

  # Kowalski, analysis
  # for i in range(input_filename.__len__()):
  #   print(input_filename[i])
  #   out_list = analyze_data(input_filename[i])
    print(input_filename[1])
    out_list = analyze_data(input_filename[1])
    # Print analysis results
    output = ""
    for char in out_list:
      output+= char
    print(output)

  # Cleanup
  if os.path.isfile("original_greek.txt"):
    os.remove("original_greek.txt")

# Actually execute the cli process for cli users
cli_process()