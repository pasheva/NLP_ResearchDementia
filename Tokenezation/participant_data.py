import nltk
from nltk.tokenize import RegexpTokenizer
from pathlib import Path
import re
import glob
import os

def extractFileName(inputPath)-> str:
    filename_w_ext = os.path.basename(inputPath)
    file_name, file_extension = os.path.splitext(filename_w_ext)
    return file_name;

def clean_up(line) -> str:
    # Removing the numbers at the end. num = 42832_46845
    line_excluding_num = re.sub(r'\d+', '', line)
    # Removing the trailing underscore from the "42832_46845"
    cleaned_sentence = line_excluding_num[:-3]
    return cleaned_sentence


def readFile(file_to_open) -> list:
    # Creating a switch to keep track of the next row.
    # If the line has just read a PAR line.
    # the value is set to True and changed back
    # to False the next line.
    switch = False

    # Opening and reading the file until the end of it.
    with open(file_to_open, "r") as file:
        data = file.readlines()
        tokenizer = RegexpTokenizer(r'[\w\']+')

        #Testing it by appending the line to a list.
        new_file_lines = []

        for line in data:
            # Removing the numbers at the end. num = 42832_46845
            cleaned_line = clean_up(line)

            # Tokenizing by removing unneeded symbols, excluding,
            # needed apostrophes such as: that's it's and etc.
            line_tokenized = tokenizer.tokenize(cleaned_line)

            if(len(line) >= 4):
                PAR_lines = line[0] + line[1] + line[2] + line[3]  # *PAR

            # print(line)
            if PAR_lines == "*PAR":
                switch = True
                line_tokenized.pop(0)
                # print(line_tokenized)
                new_file_lines.append(line_tokenized);
            elif PAR_lines != "%mor" and switch:
                new_file_lines.append(line_tokenized);
                # print(line_tokenized)
            elif PAR_lines == "%mor":
                switch = False
    return new_file_lines;


def writeFile(result_file, new_file_lines) -> None:
    with open(result_file, "w") as output:
        for listA in new_file_lines:
            output.write('%s\n' % listA)


def main():
    #Windows users need to change the path to "Dementia\cookie\*.cha"
    file_list = glob.glob("Dementia/cookie/*.cha")

    #Looping through all the files.
    for i in file_list:
        new_file_lines = readFile(i);
        output_file_name = extractFileName(i) + ".txt"
        writeFile(output_file_name, new_file_lines)


main();