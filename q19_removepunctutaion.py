import string

def remove_punctuation(input_string):
    # Create translation table to remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    
    # Use translate() method to remove punctuation
    clean_string = input_string.translate(translator)
    
    return clean_string

# Example usage:
input_string = "Hello, world! This is a test string with punctuation."

# Remove punctuation from input_string
cleaned_string = remove_punctuation(input_string)

# Print the result
print("Original string:", input_string)
print("String without punctuation:", cleaned_string)
