from nltk.corpus import stopwords   # stopwords to detect language
from nltk import wordpunct_tokenize  # function to split up our words


def get_language_likelihood(input_text):
    """Return a dictionary of languages and their likelihood of being the
    language of the comment.
    """

    input_text = input_text.lower()
    input_words = wordpunct_tokenize(input_text)

    language_likelihood = {}
    for language in stopwords._fileids:
        language_likelihood[language] = len(set(input_words) &
                                            set(stopwords.words(language)))

    return language_likelihood


def get_language(input_text):
    """Return the most likely language of the given comment"""

    likelihoods = get_language_likelihood(input_text)
    return sorted(likelihoods, key=likelihoods.get, reverse=True)[0]
