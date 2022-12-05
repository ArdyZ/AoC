import os

def readNumbers(path):
    # read as string
    data = readStrings(path)
    # convert to int
    data = [int(i) for i in data]
    return data

def readStrings(path):
    # open file
    text_file = open(path)
    # read whole file to a string
    data = text_file.read()
    
    # close file
    text_file.close()

    # convert each row to an element
    data = data.split("\n")
    return list(data)