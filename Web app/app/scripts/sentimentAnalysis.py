from detect_lang import get_language
from nltk.tokenize import RegexpTokenizer

def comments_to_list(textfile):
    """Creates a list of comments from a textfile"""
    commentlist = []
    comments = open(textfile, "r")
    for line in comments:
        commentlist.append(line)
    comments.close()
    return commentlist   

def sentiment_analysis(commentlist):
    """Calculates the sentiment of each comment and the total of all comments.
    
    Keyword arguments:
    commentlist -- a list of comments
    """
    
    total_sentiment = 0
    tokenizer = RegexpTokenizer(r'[a-z]+')
    for comment in commentlist:
        if get_language(comment) == 'english':       
            comment = comment.lower()
            #print comment
            comment = " ".join([word for word in comment.split() if  "http" not in word])        
            #print comment
            print "Language for \"{0}\" is {1}".format(comment,get_language(comment))
            words = tokenizer.tokenize(comment)
            sent_sentiment = sentiment(words)
            print sent_sentiment
            total_sentiment += sent_sentiment
        else:
                pass
        print "Total sentiment of video is %d" %total_sentiment
    return total_sentiment
        
def sentiment(words):
    """Calculaltes the sentiment score from a tokenized sentence."""
    count = 0
    for word in words:
        if word in word_dict:
            count = count + int(word_dict[word])
            #print "The word is %s and the count is %d" %(word, count)
        else:
            pass
    print "Total count is: %r" %count
    return count