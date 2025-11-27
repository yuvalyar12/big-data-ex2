"""reducer.py"""

from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)

def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin, separator=separator)
    # Store all word counts in a list
    word_counts = []
    # groupby groups multiple word-count pairs by word,
    # and creates an iterator that returns consecutive keys and their group:
    #   current_word - string containing a word (the key)
    #   group - iterator yielding all [current_word, count] items
    for current_word, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for current_word, count in group)
            word_counts.append((current_word, total_count))
        except ValueError:
            # count was not a number, so silently discard this item
            pass

    # Sort by count in descending order and take only the first 3
    word_counts.sort(key=lambda x: x[1], reverse=True)
    top_3 = word_counts[:3]
    
    # Output the top 3 words with highest counts
    for word, count in top_3:
        print("%s%s%d" % (word, separator, count))

if __name__ == "__main__":
    main()
