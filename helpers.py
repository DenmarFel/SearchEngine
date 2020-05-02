# Standard Library
import os

# Data Structures
from collections import deque

def bytesToMB(byte_size: int) -> int:
    return byte_size / (1024 ** 2) 


def printFileTotal(directory: str):
    total = 0
    for folder in os.listdir(directory):
        total += len(os.listdir(directory + "/" + folder))
    print("Amount of Files:", total)


def printDirectorySize(directory: str):
    total = 0
    for folder in os.listdir(directory):
        for domain in os.listdir(directory + "/" + folder):
            total += os.path.getsize(directory + "/" + folder + "/" + domain)
    print("Bytes:", total)
    print("MegaBytes:", total / (1024 ** 2))


def queueOfDirectoryFiles(directory: str) -> deque:
    doc_queue = []
    
    for folder in os.listdir(directory):
        for domain in os.listdir(directory + "/" + folder):
            doc_queue.append(directory + "/" + folder + "/" + domain)
    
    doc_queue.sort()
    doc_queue = deque(doc_queue)

    return doc_queue