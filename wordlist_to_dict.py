import codecs

word_dict = {}
s_line = []

wordlist = codecs.open("FINN-wordlist.txt", "r",encoding='utf8')
for line in wordlist:
    s_line.append(line.split('\t'))
wordlist.close()

for w,n in s_line:
    word_dict[w] = n

#print word_dict['limited']