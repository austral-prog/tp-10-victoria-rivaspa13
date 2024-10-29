def unique_strings(input_string):
    unique_chars = []  
    for char in input_string:
        if char not in unique_chars:
            unique_chars.append(char)  
    return unique_chars
