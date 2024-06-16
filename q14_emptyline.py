def read_and_print_lines():
    lines = []
    while True:
        line = input("Enter a line (press Enter to finish): ")
        if line == "":
            break
        lines.append(line)
    
    print("\nEntered lines:")
    for line in lines:
        print(line)

# Example usage:
read_and_print_lines()
