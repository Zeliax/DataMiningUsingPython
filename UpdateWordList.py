# -*- coding: utf-8 -*-
"""Includes the function to update the score in the word list."""


def dict_translator(filename):
    """Translate the original values to only positive values."""
    dict_file = open(filename, 'r')
    outputs = []
    for line in dict_file:
        outputs.append(line.split('\t'))
    dict_file.close()

    dict_file = open(filename, 'w')
    for output in outputs:
        output[1] = int(output[1]) + 5
        dict_file.write(output[0] + '\t' + str(output[1]) + '\n')
    dict_file.close()


def main():
    """Testing."""
    dict_translator('FINN-wordlist.txt')

if __name__ == '__main__':
    main()
