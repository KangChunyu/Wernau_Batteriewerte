# Wernau Data Processing

## Features

- **Validate Timestamps**: The system checks if the timestamps in the dataset are in the correct 15-minute intervals.
- **Column Extraction**: Allows the user to select columns to extract from the data.
- **Output to Excel**: Extracted data is saved in an Excel file (`.xlsx` format).
- **File Validation**: Ensures the data files have a valid structure before processing.

## Requirements

To run this project, you need the following Python packages:

- `pandas`: For data handling and writing to Excel files.
- `openpyxl`: Excel writer support for `pandas`.

To install these packages, create a `requirements.txt` file by running:

```bash
pip install -r requirements.txt

## How to Use

- Open Terminal, Type python main.py and follow the instructions in the Terminal 