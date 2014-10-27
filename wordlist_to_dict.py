import codecs
word_dict = {}

def wordlist_to_dict(list):
    
    s_line = []
    wordlist = codecs.open(list, "r",encoding='utf8')
    for line in wordlist:
        s_line.append(line.split('\t'))
    wordlist.close()

    for w,n in s_line:
        word_dict[w] = n

#wordlist_to_dict("FINN-wordlist.txt")
#print word_dict['limited']