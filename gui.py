# import the gui library
import PySimpleGUI as simpleGUI
import os.path

# create variables to hold relevant values
quote_file_name = ""
quote_text = ""

# create components for the input (left) side
input_column = [
  [
    simpleGUI.Text("Select quotation file:"),
    simpleGUI.Input(key = "-QUOTATION_FILE-", enable_events = True),
    simpleGUI.FileBrowse(button_text = "Browse", target = "-QUOTATION_FILE-"),
  ],
  [
    simpleGUI.Text("OR"),
  ],
  [
    simpleGUI.Text("Type/paste quotation here:"),
    simpleGUI.Input(size = (50, 4), enable_events = True, key = "-QUOTATION_TEXT-"),
  ],
  [
    simpleGUI.Submit(button_text = "Find Verse"),
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
    quote_file_name = values["-QUOTATION_FILE-"]
    window["-OUTPUT-"].update(quote_file_name)
  elif event == "-QUOTATION_TEXT-":
    quote_text = values["-QUOTATION_TEXT-"]
    window["-OUTPUT-"].update(quote_text)
window.close()