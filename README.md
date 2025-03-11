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

# Clone the repository
git clone <your-repo-url>
cd <repository-name>

# (Optional) Create and activate a virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create an output folder
mkdir output

# Run the script and save output
python main.py > output/result.txt
