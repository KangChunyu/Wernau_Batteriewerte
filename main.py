import os
import csv
import pandas as pd
from datetime import datetime, timedelta

# Function to validate timestamps in a file
def validate_timestamps(data):
    timestamps = [datetime.strptime(row[0], "%d.%m.%Y %H:%M") for row in data]
    
    start_month = timestamps[0].month
    start_year = timestamps[0].year

    next_month = (start_month % 12) + 1
    next_month_year = start_year + (1 if start_month == 12 else 0)

    expected_start_time = datetime(start_year, start_month, 1, 0, 15)
    expected_end_time = datetime(next_month_year, next_month, 1, 0, 0)

    expected_timestamps = []
    current_time = expected_start_time
    while current_time < expected_end_time:
        expected_timestamps.append(current_time)
        current_time += timedelta(minutes=15)

    # Find missing timestamps
    missing_timestamps = [ts for ts in expected_timestamps if ts not in timestamps]

    if missing_timestamps:
        return False, f"Missing timestamps: {', '.join([ts.strftime('%d.%m.%Y %H:%M') for ts in missing_timestamps])}"

    return True, "Validation passed."

# Function to validate a single file and extract data
def validate_file(input_file, col1=None, col2=None):
    with open(input_file, 'r', encoding='latin1') as file:
        lines = file.readlines()

    header_index = None
    for i, line in enumerate(lines):
        if line.strip().startswith("Datum/Zeit"):
            header_index = i
            break

    if header_index is None:
        return False, "No header found."

    data_lines = lines[header_index:]
    reader = csv.reader(data_lines, delimiter=';')
    header = next(reader)

    extracted_data = []
    for row in reader:
        if len(row) >= len(header) and all(cell.strip() for cell in row):
            extracted_data.append(row)
        else:
            return False, "Missing data in one or more columns."

    valid, message = validate_timestamps(extracted_data)
    if not valid:
        return False, message  # Now correctly returns missing timestamp error!

    if col1 and col2:
        if col1 not in header or col2 not in header:
            return False, f"Invalid columns selected. Available: {', '.join(header)}"

        timestamp_idx = header.index("Datum/Zeit")
        col1_idx = header.index(col1)
        col2_idx = header.index(col2)

        processed_data = [["Datum/Zeit", col1, col2]]
        for row in extracted_data:
            if len(row) > max(timestamp_idx, col1_idx, col2_idx):
                processed_data.append([row[timestamp_idx], row[col1_idx], row[col2_idx]])

        return True, processed_data

    return True, header  # Return header if no columns are selected yet

# Validate all files in a folder
def validate_folder(folder_path):
    valid_files = []
    log = []

    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"):
            input_file = os.path.join(folder_path, file_name)
            
            valid, message = validate_file(input_file)
            if not valid:
                log.append(f"{file_name}: {message}")
                continue

            valid_files.append(file_name)

    if log:
        print("\nInvalid Files:")
        for entry in log:
            print(entry)

    if valid_files:
        print("\nValid Files:")
        for valid_file in valid_files:
            print(valid_file)

    return valid_files

# Process and save extracted data
def process_files(files, input_folder, col1, col2, output_folder, output_file="Wernau_Output.xlsx"):
    all_data = []
    header = ["Datum/Zeit", col1, col2]

    for file in files:
        file_path = os.path.join(input_folder, file)
        valid, data = validate_file(file_path, col1, col2)

        if not valid:
            print(f"Skipping {file}: {data}")
            continue

        all_data.extend(data[1:])  # Append without header to avoid duplicates

    if all_data:
        output_file_path = os.path.join(output_folder, output_file)
        df = pd.DataFrame(all_data, columns=header)
        df.to_excel(output_file_path, index=False)
        print(f"\nAll data saved to {output_file_path}.")
    else:
        print("\nNo valid data to save.")

# Main function
def main():
    input_folder = input("Enter the folder path containing the files: ").strip()

    if not os.path.exists(input_folder):
        print("Folder does not exist. Exiting.")
        return

    print("\nValidating files...")
    valid_files = validate_folder(input_folder)

    if not valid_files:
        print("No valid files found. Exiting.")
        return

    print("\nWhich files do you want to process? (comma-separated)")
    user_input = input("> ").strip()
    files_to_process = [file.strip() for file in user_input.split(",") if file.strip() in valid_files]

    if not files_to_process:
        print("No valid files selected. Exiting.")
        return

    # Extract header from the first selected file
    sample_file = os.path.join(input_folder, files_to_process[0])
    with open(sample_file, 'r', encoding='latin1') as file:
        lines = file.readlines()

    header_index = None
    for i, line in enumerate(lines):
        if "Datum/Zeit" in line:
            header_index = i
            break

    if header_index is None:
        print("No header found.")
        return

    data_lines = lines[header_index:]
    reader = csv.reader(data_lines, delimiter=';')
    header = next(reader)

    # Print available columns
    print("\nAvailable columns:")
    for col in header:
        print(col)

    col1 = input("\nEnter the first column name to extract: ").strip()
    col2 = input("Enter the second column name to extract: ").strip()

    if col1 not in header or col2 not in header:
        print(f"Invalid column names. Please choose from: {', '.join(header)}")
        return

    # Prompt for output folder path
    while True:
        output_folder = input("\nEnter the folder path to save the output file: ").strip()
        if os.path.exists(output_folder):
            break
        print("Folder does not exist. Please enter a valid folder path.")

    print("\nProcessing files...")
    process_files(files_to_process, input_folder, col1, col2, output_folder) #Pass output_folder for output file

if __name__ == "__main__":
    main()
