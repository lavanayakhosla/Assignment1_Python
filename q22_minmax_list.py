def find_min_max(numbers):
    if not numbers:
        return None, None  # Return None for both min and max if list is empty
    
    minimum = min(numbers)
    maximum = max(numbers)
    return minimum, maximum


