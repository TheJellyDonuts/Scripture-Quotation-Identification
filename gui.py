'''
Kobe Couvion
03-06-2023

~ ~ GUI ~ ~
Purpose:
  Provide an easy to use interface for an end
  user to interact with the scripture quotation
  identification tool. The goal for this GUI is
  to generate a stand-alone executable such that
  a user with little to no technical knowledge
  can easily run the program without worrying
  about any extra configurations for their machine.
Dev Help:
  This GUI implements features of the PySimpleGUI
  library, which provides an event-driven interface
  to the user based primarily on key presses and
  button click events. The event loop manages the
  actions to take for each possible event, and the
  data associated with each event key. For library
  info, visit pysimplegui.org.
'''


# Import the gui library
import PySimpleGUI as simpleGUI
import os.path
import source_parser

# Create variables to hold relevant values
quote_file_name = None
quote_text = None
verse_data = None

# Create relevant functions to perform relevant tasks


# Create components for the input (left) side
input_column = [
  [
    simpleGUI.Text("Select quotation file:"),
    # Allow the user to choose a file to hold the input quotation
    simpleGUI.Input(key = "-QUOTATION_FILE-", enable_events = True),
    simpleGUI.FileBrowse(button_text = "Browse", target = "-QUOTATION_FILE-", file_types=(("Text Files", "*.txt"))),
  ],
  [
    simpleGUI.Text("OR"),
  ],
  [
    # Allow the user to simply paste a quotation as input
    simpleGUI.Text("Type/paste quotation here:"),
    simpleGUI.Input(size = (50, 4), enable_events = True, key = "-QUOTATION_TEXT-"),
  ],
  [
    # Button to parse the input quotation and display the results
    simpleGUI.Submit(button_text = "Find Verses", key = "-SUBMIT-"),
  ],
]

# Create components for the output (right) side
output_column = [
  [
    simpleGUI.Text("Matching verse(s):"),
  ],
  [
    # Create a window for displaying the matching verses
    simpleGUI.Output(key = "-OUTPUT-"),
  ],
  [
    # Provide helpful buttons for the user
    simpleGUI.Help("Help"),
    simpleGUI.Exit("Exit"),
  ],
]

# Create the layout using our columns
layout = [
  [
    simpleGUI.Column(input_column),
    simpleGUI.VSeperator(),
    simpleGUI.Column(output_column),
  ],
]

# Create the window using our layout and a cool theme
simpleGUI.theme("SandyBeach")
window = simpleGUI.Window("Scripture Quotation Identification", layout)

# Run the event loop
while True:
  event, values = window.read()

  # Close the window when appropriate
  if event == "Exit" or event == simpleGUI.WIN_CLOSED:
    break

  # Update the user's input file name
  elif event == "-QUOTATION_FILE-":
    quote_file_name = values["-QUOTATION_FILE-"]
    if os.path.isfile(quote_file_name):
      # Process the input file and display the matching verses for the quotation
      verse_data = source_parser.parseGreek(quote_file_name)
      window["-OUTPUT-"].update(verse_data)
    else:
      # Throw an exception for a nonexistent file
      window["-OUTPUT-"].update("ERROR: File does not exist")
  elif event == "-QUOTATION_TEXT-":
    quote_text = values["-QUOTATION_TEXT-"]
    window["-OUTPUT-"].update(quote_text)

window.close()