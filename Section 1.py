import math
from collections import defaultdict


def Cipher(input):
    text = input.replace(" ", "")  # remove any empty spaces from our text
    length = len(text)
    root = math.sqrt(length)

    # math.floor and math.ceil function to calculate the required number of rows and columns
    rows = math.floor(root)
    columns = math.ceil(root)
    matrix = defaultdict(str)  # initialize an empty dictionary using defualtdict which never raises a KeyError

    # divide our string into equal number of columns
    for row in range(0, len(text), columns):
        sub = text[row:row + columns]  # slicing the string
        for column in range(len(sub)):
            matrix[column] += sub[column]
    return list(matrix.values())


# Number of times code will cipher the message
num = input("Enter Number of Ciphertexts: ")
num_of_ciphers = int(num)
while num_of_ciphers > 0:
    print(*Cipher(input()))  # used to capture an unlimited number of positional arguments given to the function
    num_of_ciphers -= 1
    
    

