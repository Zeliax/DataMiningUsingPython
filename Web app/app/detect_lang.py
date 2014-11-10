from nltk.corpus import stopwords   # stopwords to detect language
from nltk import wordpunct_tokenize  # function to split up our words


class LanguageDetector(object):
    """Detects the language of a given string"""
    def __init__(self):
        self.lang_stopwords = {language: set(stopwords.words(language))
                               for language in stopwords._fileids}

    def get_language_likelihood(self, input_text):
        """Return a dictionary of languages and their likelihood of being the
        language of the comment.
        """
        input_text = input_text.lower()
        input_words = wordpunct_tokenize(input_text)
        language_likelihood = {}
        for language, stopword_set in self.lang_stopwords.items():
            language_likelihood[language] = len(set(input_words) & stopword_set)
        return language_likelihood

    def get_language(self, input_text):
        """Return the most likely language of the given comment"""
        likelihoods = self.get_language_likelihood(input_text)
        return sorted(likelihoods, key=likelihoods.get, reverse=True)[0]
