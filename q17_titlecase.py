def convert_to_title_case(input_string):
    # Split the string into words and capitalize each word
    words = [word.capitalize() for word in input_string.split()]
    
    # Join the capitalized words back into a single string
    title_case_string = " ".join(words)
    
    return title_case_string

# Example usage:
input_string = "hello world! this is a test string."

# Convert input_string to title case
title_case_result = convert_to_title_case(input_string)

# Print the result
print("Original string:", input_string)
print("Title case string:", title_case_result)
