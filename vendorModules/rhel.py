import re

def rhel (title):
    # Define a regular expression pattern to match text inside square brackets
    pattern = r'\[([^\]]+)\]'

    # Use re.search() to find the pattern in the input string
    match = re.search(pattern, title)

    # Extract and print the matched text
    if match:
        extracted_text = match.group(1)
        #print(extracted_text)
    else:
        print("Pattern not found in the input string.")

    return extracted_text