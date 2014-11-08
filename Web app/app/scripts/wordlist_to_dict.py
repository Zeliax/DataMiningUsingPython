import codecs
word_dict = {}

def wordlist_to_dict(list):
    """Creates a dictionary from a wordlist"""
    s_line = []
    wordlist = codecs.open(list, "r",encoding='utf8')
    for line in wordlist:
        s_line.append(line.split('\t'))
    wordlist.close()

    for w,n in s_line:
        word_dict[w] = n
    return word_dict
#wordlist_to_dict("FINN-wordlist.txt")
#print word_dict['limited']