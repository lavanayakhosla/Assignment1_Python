def count_character_frequency(input_string):
    # Initialize an empty dictionary to store character frequencies
    frequency_dict = {}
    
    # Iterate through each character in the input string
    for char in input_string:
        # Increment the count of character in the dictionary
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1
    
    return frequency_dict

# Example usage:
input_string = "hello world"

# Count frequency of each character in input_string
frequency_dict = count_character_frequency(input_string)

# Print the result
print("Character frequencies in the string:")
for char, count in frequency_dict.items():
    print(f"'{char}' : {count}")
