import nltk
from nltk.tokenize import RegexpTokenizer
from pathlib import Path
import re

# Path to the files.
dementia_data_folder = Path("Dementia/cookie")
file_to_open = dementia_data_folder / "005-2.cha"


def clean_up(line):
    # Removing the numbers at the end. num = 42832_46845
    line_excluding_num = re.sub(r'\d+', '', line)
    # Removing the trailing underscore from the "42832_46845"
    cleaned_sentence = line_excluding_num[:-3]
    return cleaned_sentence


# Creating a switch to keep track of the next row.
# If the line has just read a PAR line.
# the value is set to True and changed back
# to False the next line.
switch = False

# Opening and reading the file until the end of it.
with open(file_to_open) as file:
    data = file.readlines()
    tokenizer = RegexpTokenizer(r'[\w\']+')

    for line in data:
        # Removing the numbers at the end. num = 42832_46845
        cleaned_line = clean_up(line)

        # Tokenizing by removing unneeded symbols, excluding,
        # needed apostrophes such as: that's it's and etc.
        line_tokenized = tokenizer.tokenize(cleaned_line)

        PAR_lines = line[0] + line[1] + line[2] + line[3]  # *PAR

        # print(line)
        if PAR_lines == "*PAR":
            switch = True
            line_tokenized.pop(0)
            print(line_tokenized)
        elif PAR_lines != "%mor" and switch:
            print(line_tokenized)
        elif PAR_lines == "%mor":
            switch = False
