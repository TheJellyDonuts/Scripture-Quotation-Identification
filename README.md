# Scripture-Quotation-Identification

Given a scripture quotation from a church father's writings[^1], identify the most likely verses being quoted by that quotation, each with a percent confidence according to the algorithms we implemented.

<add stuff about using the various interfaces>

---

## <ins>Prerequisites</ins>
1. Python 3.X (3.10+ was used in development)
2. Python libraries detailed in `requirements.txt`. To install the libraries collectively, run the following terminal command:
> `pip -r requirements.txt`

---

## <ins>Instructions for Use</ins>
### CLI:
To analyze a string of raw Greek text:

    python <cli_filepath>/cli.py -t "<Greek_text>"

To analyze a file containing Greek text:

    python <cli_filepath>/cli.py -f <Greek_filepath>

To analyze multiple files containing Greek text:

    python <cli_filepath>/cli.py -b <Greek_filepath_1> <Greek_filepath_2> ...

### GUI:
1. Run the GUI: `python <gui_filepath>/gui.py`
2. Use your preferred method to input the Greek quotation.
3. Click the `Find Verses` button to analyze the quotation for potenial verse references.

[^1]: Link to apostolic-fathers repo: https://github.com/jtauber/apostolic-fathers
