
file_name = "example.txt"

try:

    with open(file_name, 'r') as file:
      
        file_content = file.read()
    
        print("File content:")
        print(file_content)
        
except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist.")
except PermissionError:
    print(f"Error: You do not have permission to read the file '{file_name}'.")
except Exception as e:
    print(f"Error: An unexpected error occurred - {str(e)}")
