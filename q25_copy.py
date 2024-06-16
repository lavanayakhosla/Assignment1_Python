def copy_file(source_file, destination_file):
    try:
        # Open the source file in read mode
        with open(source_file, 'r') as source:
            # Read the contents of the source file
            contents = source.read()
        
        # Open the destination file in write mode
        with open(destination_file, 'w') as destination:
            # Write the contents to the destination file
            destination.write(contents)
        
        print(f"Successfully copied contents from '{source_file}' to '{destination_file}'.")
    
    except FileNotFoundError:
        print(f"Error: One of the files ('{source_file}' or '{destination_file}') not found.")
    except PermissionError:
        print(f"Error: Permission denied to access files ('{source_file}' or '{destination_file}').")
    except Exception as e:
        print(f"Error: An unexpected error occurred - {str(e)}")
