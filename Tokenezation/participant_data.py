import nltk
from nltk.tokenize import RegexpTokenizer
from pathlib import Path

dementia_data_folder = Path("Dementia/cookie")
file_to_open = dementia_data_folder/"001-0.cha"

with open(file_to_open) as file:
    data = file.readlines()
    tokenizer = RegexpTokenizer(r'[\w\']+')
    # Creating a switch to keep track of the next row.
    for line in data:
        line_tokenized = tokenizer.tokenize(line)
        # print(line_tokenized[0])
        PAR_lines = line[0]+line[1]+line[2]+line[3]
        if PAR_lines == "*PAR":
            # Removing the numbers at the end. 42832_46845

            print(line_tokenized)
