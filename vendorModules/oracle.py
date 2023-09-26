import re

def oracle (title):
    # Define a regular expression pattern to match text inside square brackets
    pattern = r'ELSA-(\d{4})-(\d{4})'


    # Use re.search() to find the pattern in the input string
    match = re.search(pattern, title)

    # Extract and print the matched text
    if match:
        extracted_text = match.group()
        #print(extracted_text)
    else:
        print("Pattern not found in the input string.")

    return extracted_text