# -*- coding: utf-8 -*-


def dict_translator(filename):
    dict_file = open(filename, 'r')
    outputs = []
    for line in dict_file:
        outputs.append(line.split('\t'))
    dict_file.close()

    dict_file = open(filename, 'w')
    for output in outputs:
        output[1] = int(output[1]) + 6
        dict_file.write(output[0] + '\t' + str(output[1]) + '\n')
    dict_file.close()


def main():
    """
    Testing
    """
    dict_translator('FINN-wordlist.txt')

if __name__ == '__main__':
    main()
