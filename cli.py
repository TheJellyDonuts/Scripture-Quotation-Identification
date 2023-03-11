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
import src.prob_data as prob_data
import src.prob_analysis as prob_analysis
import argparse

# Create a temp file for greek input text
def read_in_greek(original_greek: str):
    with open("original_greek.txt", "w", encoding="utf-8") as f:
        f.write(original_greek)
        return f.name

# Sanitize input file/text BEFORE ANYTHING ELSE
def sanitize_input(input: str, is_file: bool):
    extension: str = os.path.splitext(input)[1]
    if is_file:
        # Check that file exists and is not harmful
        if not os.path.isfile(input):
            raise Exception("File does not exist")
        elif extension != ".txt":
            raise Exception("Only .txt files are acceptable.")
        elif os.stat(input).st_size > 1073741824:
            raise Exception("File size must be smaller than 1GB")
        else:
            # TODO: Handle malicious file catching
            return
    else:
        # TODO: Handle malicious text catching
        return

# Do the probability analysis
def analyze_data(filename: str, sd=3):
    # Parse the input and generate probabilit data
    prob_data.synthesize(filename)
    # Analyze the probability data against the Greek New Testament
    output_list = prob_analysis.average_analysis(True, sd)
    return output_list

# Dump the analysis output into a text file
def generate_output(input_filename: str, output_list: list):
    input_filename = os.path.basename(input_filename)
    #  Create output file
    output_filename: str = ""
    if input_filename == "original_greek.txt":
        output_filename = "quotation_analysis.txt"
    else:
        output_filename = os.path.splitext(input_filename)[0] + "_analysis.txt"
    output_rel_path = "output/"
    output_file_path = os.path.join(output_rel_path, output_filename)
    with open(output_file_path, "w", encoding='utf-8') as f:
        # Write analysis results to output file
        for i in range(output_list.__len__()):
            # Write the verse that best matches it
            f.write(output_list[i])

    # Close file and inform user
    print("Quotation analyzed.")
    print("Analysis written to " + output_filename + ".")

# Run the interface through the command line


def cli_process():
    # Adds Arguments to the command line
    parser = argparse.ArgumentParser(
        description='Find Possible New Testament Quotations in Greek Manuscripts')
    parser.add_argument('-o', '--output', action='store_true',
                        help='Redirects output to a file')
    parser.add_argument('-f', '--file', type=str, nargs='+',
                        help='Specifies input file path')
    parser.add_argument('-i', '--input', type=str, nargs=1,
                        help='Enter text directly following this tag')
    parser.add_argument('-sd', type=int, nargs=1,
                        help='Specify integer for number of standard deviations to include')

    # Get arguments
    args = parser.parse_args()

    # Sanitize input and grab filename(s)
    input_filename = []

    # If -f or --file is set, analyze files
    if (args.file):
        for i in range(0, len(args.file)):
            sanitize_input(args.file[i], True)
            input_filename.append(args.file[i])
    # If text is set, analyze files
    elif (args.input):
        sanitize_input(args.input[0], False)
        input_filename.append(read_in_greek(args.input[0]))
    else:
        raise Exception("Input must be specified")

    # Kowalski, analysis
    for i in range(input_filename.__len__()):
        print(input_filename[i])

        # Checks if Standard Deviation Flag is used
        if (args.sd):
            out_list = analyze_data(input_filename[i], args.sd[0])
        else:
            out_list = analyze_data(input_filename[i])

        # Generate Text Files that contain output
        if (args.output):
            generate_output(input_filename[i], out_list)
        else:
            # Print analysis results
            output = ""
            for char in out_list:
                output += char
            print(output)

        # Cleanup
        if os.path.isfile("original_greek.txt"):
            os.remove("original_greek.txt")

# Run the interface through the web app


def web_process(input: str):
    sanitize_input(input)
    f = read_in_greek(input)
    o = analyze_data(f)
    # Cleanup
    os.remove("original_greek.txt")
    return o


# Actually execute the cli process for cli users
cli_process()
