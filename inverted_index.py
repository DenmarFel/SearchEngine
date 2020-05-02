# Standard Library
import os
import sys
import json
import pickle
import time
import re

# Other Libraries
from bs4 import BeautifulSoup

import helpers

# Data Structures
from collections import deque
from term_dict import TermDict
from postings import Posting


def offLoadPartialIndx(partial_indx: dict, num: int):
    file_name = "partial_indexes/inverted_indx{}".format(num)
    with open(file_name, "wb") as open_file:
        pickle.dump(partial_indx, open_file)
        print("Created:", file_name)


def constructPartialIndex(directory: str):
    partial_indx = {}
    partial_indx_qty = 1
    
    doc_queue = helpers.queueOfDirectoryFiles(directory)
    doc_id = 1
    while doc_queue:
        doc = doc_queue.popleft()
        with open(doc) as doc_file: data = json.load(doc_file)

        soup = BeautifulSoup(data["content"], 'html.parser')
        term_dict = TermDict()
        term_dict.update(soup)
        for word, count in term_dict.getTermDict().items():
            if word not in partial_indx:
                partial_indx[word] = [Posting(doc_id, count)]
            else:
                partial_indx[word].append(Posting(doc_id, count))
        
        # print(helpers.bytesToMB(sys.getsizeof(partial_indx)))
        # print(soup.prettify())
        # print(partial_indx["the"])
        # if helpers.bytesToMB(sys.getsizeof(partial_indx)) >= 0.1:
        #     offLoadPartialIndx(partial_indx, partial_indx_qty)
        #     partial_indx = {}
        #     partial_indx_qty += 1
        
        doc_id += 1
       
        

def constructInvertedIndex(directory: str):
    helpers.printFileTotal(directory)
    helpers.printDirectorySize(directory)

    constructPartialIndex(directory)


if __name__ == "__main__":
    try:
        # directory = sys.argv[1]
        directory = "DEV"
    
    except IndexError:
        print("[ERROR] Failed to provide a root directory.")
        directory = input("Please enter a root directory to construct inverted index: ")

    finally:
        constructInvertedIndex(directory)
                