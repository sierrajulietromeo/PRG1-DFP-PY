import os

def parse_file(input_file_path, output_file_path, max_description_length, delimiter=","):
    
  # Check if the input file exists
    if not os.path.exists(input_file_path):
        return -1

    # Check if the output file exists and delete it if it does
    if os.path.exists(output_file_path):
        os.remove(output_file_path)

    # Open the input file and read its contents
    with open(input_file_path, mode='r', encoding='utf-8') as infile:
        lines = infile.readlines()

    # Process each line (skip the header)
    processed_holidays = []
    for line in lines[1:]:  # Skip the header row
        # Split the line into columns using the delimiter
        row = line.strip().split(delimiter)

        # Extract required columns
        holiday_id = row[0].strip()
        destination = row[1].strip()
        description = row[2].strip()
        price = row[3].strip()

        # Truncate the description if necessary
        if len(description) > max_description_length:
            description = description[:max_description_length - 3] + "..."

        # Re-order columns
        processed_row = [holiday_id, price, destination, description]
        processed_holidays.append(processed_row)

    # Write the processed data to the output file
    with open(output_file_path, mode='w', encoding='utf-8') as outfile:
        for row in processed_holidays:
            # Join the columns with the delimiter and write to the file
            outfile.write(delimiter.join(row) + '\n')

    # Return the total number of holidays processed
    return len(processed_holidays)


