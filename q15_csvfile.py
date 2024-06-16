import csv

def read_csv_file(file_path):
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")

# Example usage:
file_path = 'data.csv'  # Replace with your CSV file path
read_csv_file(file_path)
