# import the gui library
import PySimpleGUI as simpleGUI
import os.path

# create variables to hold relevant values
quote_file_name = ""
quote_text = ""

# create relevant functions to perform relevant tasks


# create components for the input (left) side
input_column = [
  [
    simpleGUI.Text("Select quotation file:"),
    # Allow the user to choose a file to hold the input quotation
    simpleGUI.Input(key = "-QUOTATION_FILE-", enable_events = True),
    simpleGUI.FileBrowse(button_text = "Browse", target = "-QUOTATION_FILE-"),
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

# create components for the output (right) side
output_column = [
  [
    simpleGUI.Text("Matching verse(s):"),
  ],
  [
    simpleGUI.Output(key = "-OUTPUT-"),
  ],
  [
    simpleGUI.Help("Help"),
    simpleGUI.Exit("Exit"),
  ],
]

# create the layout using our columns
layout = [
  [
    simpleGUI.Column(input_column),
    simpleGUI.VSeperator(),
    simpleGUI.Column(output_column),
  ],
]

# create the window using our layout
simpleGUI.theme("SandyBeach")
window = simpleGUI.Window("Scripture Quotation Identification", layout)

# run the event loop
while True:
  event, values = window.read()
  if event == "Exit" or event == simpleGUI.WIN_CLOSED:
    break
  elif event == "-QUOTATION_FILE-":
    # Grab the user-inputted file name and make sure it exists
    quote_file_name = values["-QUOTATION_FILE-"]
    if os.path.isfile(quote_file_name):
      # Display the file's text in the output window
      window["-OUTPUT-"].update(quote_file_name)
    else:
      # Throw an exception for a nonexistent file
      window["-OUTPUT-"].update("ERROR: File does not exist")
  elif event == "-QUOTATION_TEXT-":
    quote_text = values["-QUOTATION_TEXT-"]
    window["-OUTPUT-"].update(quote_text)

window.close()