# Scripture-Quotation-Identification

Given a scripture quotation from a church father's writings[^1], identify the most likely verses being quoted by that quotation, ideally with a level of confidence according to the algorithms we implemented.

---

## <ins>Prerequisites</ins>
**These prerequisites are only necessary if running individual .py files**
1. Python 3.X (3.10+ was used in development)
2. Python libraries detailed in `requirements.txt`. To install the libraries collectively, run the following terminal command:
    - `pip -r requirements.txt`

---

## <ins>Instructions for Use</ins>
### CLI:
To analyze a string of raw Greek text:
> NOTE: the current working directory should be in the folder where `SQI.exe` is located

`SQI.exe -i "<Greek_text>"`

To analyze a single file containing Greek text:

`SQI.exe -f <Greek_filepath>`

To analyze multiple files containing Greek text:

`SQI.exe -f <Greek_filepath_1> <Greek_filepath_2> ...`

To output data to a file:

`SQI.exe -f <Greek_filepath> -o`

To specify the number of standard deviations:

`SQI.exe -f <Greek_filepath> -sd <number_of_standard_dev>`

### GUI:
1. Run the GUI: `python <gui_filepath>/gui.py` (ensure that the [prerequisites](https://github.com/TheJellyDonuts/Scripture-Quotation-Identification#prerequisites) are fulfilled before running!)
2. Use your preferred method to input the Greek quotation.
3. Click the `Find Verses` button to analyze the quotation for potential verse references.

### WUI:
*Work in progress. Needs further server development.*

---

## <ins>[Wiki](https://github.com/TheJellyDonuts/Scripture-Quotation-Identification/wiki)</is>
Visit the [Wiki](https://github.com/TheJellyDonuts/Scripture-Quotation-Identification/wiki) to learn more about how our program parses and analyzes all of the information! Documentation is available for all of the major classes.

### Future Goals
- [ ] Migrate to tempfile Python Library Where Necessary
- [ ] Organize Source Code into src/ Directory
- [ ] Implement CLI & GUI & WUI Loading Bar
- [ ] Build Pen Test Cases
- [ ] Create Task List for Word Order Algorithm


[^1]: Link to apostolic-fathers repo: https://github.com/jtauber/apostolic-fathers
