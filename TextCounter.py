import re

## LOADING THE FILE 

def load_myfile(myfile_path):
    with open(myfile_path, 'r') as file:
        content = file.read()
    return content

## COUNT THE WORDS FROM THE FILE

def count_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

## SAVING THE REPORT 

def save_report(word_counts, output_newfile):
    sorted_wordcounts = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
    with open(output_newfile, 'w') as file:
        for word, count in sorted_wordcounts:
            file.write(f"{word}: {count}\n")

## MAIN FUNCTION

def main(input_myfile, output_newfile):
    data = load_myfile(input_myfile)
    word_counts = count_words(data)
    save_report(word_counts, output_newfile)
    
## SPECIFYING INPUT AND OUTPUT FILES
input_myfile = r"D:\SEMESTER 2 GC\Python\assignment1\sample.txt"
output_newfile = r"D:\SEMESTER 2 GC\Python\assignment1\word_frequency_report.txt"

main(input_myfile, output_newfile)



