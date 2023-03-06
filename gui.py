# import the gui library
import PySimpleGUI as simpleGUI
import os.path

# create components for the input (left) side
input_column = [
  [
    simpleGUI.Text("Select quotation file"),
    simpleGUI.FolderBrowse(button_text = "Browse"),
    simpleGUI.Text(),
  ],
  [
    simpleGUI.Text("OR"),
  ],
  [
    simpleGUI.Text("Type/paste quotation here:"),
    simpleGUI.Input(size = (50, 4), enable_events = True, key = "-QUOTATION_TEXT-")
  ],
]

output_column = [
  [
    simpleGUI.Text("Matching verse(s):"),
  ],
  [
    simpleGUI.Output(),
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
window = simpleGUI.Window("Scripture Quotation Identification", layout)

# run the event loop
while True:
  event, values = window.read()
  if event == "Exit" or event == simpleGUI.WIN_CLOSED:
    break
window.close()