# Wernau Data Processing

## Features

- **Validate Timestamps**: The system checks if the timestamps in the dataset are in the correct 15-minute intervals.
- **Column Extraction**: Allows the user to select columns to extract from the data.
- **Output to Excel**: Extracted data is saved in an Excel file (`.xlsx` format).
- **File Validation**: Ensures the data files have a valid structure before processing.

## How to Use this Project

To run this project, you need the following Python packages:

- `Python`: Need to install Python first for running the program. -> https://www.python.org/downloads/
- `Git`: Install Git to be able to clone the repository -> https://git-scm.com/downloads
- `pandas`: For data handling and writing to Excel files.
- `openpyxl`: Excel writer support for `pandas`.

## How to Use the Project

### Clone the repository to your Desktop
`git clone https://github.com/KangChunyu/Wernau_Batteriewerte.git $HOME\Desktop\Wernau_Batteriewerte`

### Direct to the designate cloned Folder 
`cd $HOME\Desktop\Wernau_Batteriewerte`

### (Optional) Create and activate a virtual environment
`python -m venv venv` 
and
`venv\Scripts\activate`

### Install dependencies
`pip install -r requirements.txt`

### Run the script and save output
'python main.py'
