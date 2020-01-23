from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
from nltk.corpus import brown
from collections import Counter
from nltk.stem import WordNetLemmatizer
import nltk

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def remove_stopwords(word_list):
    new_list = []
    for word in word_list:
        if word not in stop_words:
            new_list.append(word)
    return new_list


def lemmatize_words(word_list):
    new_list = []
    for word in word_list:
        new_list.append(lemmatizer.lemmatize(word))

def promptUser():
    return input(
            "Options:\n1)With stopwords\n2)Without stopwords\n3)Without stopwords and lemmatization\n4)Without stopwords and stemming\n" +
            "Please choose an mode: "
            )

mode = -1
if mode != 1 or mode != 2 or mode != 3 or mode != 4:
    mode = promptUser()

for category in brown.categories():
    words = brown.words(categories=category)
    print(len(words))

    if mode == '1':
        word_list_tagged = nltk.pos_tag(words)
        total_word_tokens = len(words)
    else:
        without_stopwords = remove_stopwords(words)
        word_list_tagged = nltk.pos_tag(without_stopwords)
        total_word_tokens = len(without_stopwords)

    types = nltk.FreqDist(tag for (word, tag) in word_list_tagged)

    print('****************************** ' + category + ' ******************************')
    print(' -This category has ' + str(total_word_tokens) + ' word tokens')
    # word_list_tagged = brown.tagged_words(categories=category) # add , tagset='universal' for the basic types only
    # words = brown.words(categories=category)
    # without_stopwords = remove_stopwords(words)


    # lemmed = []
    # for w in without_stopwords:
    #     lemmed.append(lemm.lemmatize(w))

    # y = nltk.pos_tag(lemmed)
    # lemmed_tagged = nltk.FreqDist(tag for (word, tag) in y)

    # print('****************************** ' + category + ' ******************************')
    # print(' -This category has ' + str(len(words)) + ' word tokens including all stopwords')
    # print(' -This category has ' + str(len(word_list_tagged)) + ' word tokens including all stopwords')
    # print(' -This category has ' + str(len(without_stopwords)) + ' word tokens NOT including all stopwords')
    print(' -This category has ' + str(len(types.most_common())) + ' word types')
    # print(' -This category has ' + str(len(lemmed_tagged.most_common())) + ' word types')
    # print(' -This category has ' + str(len(lemmed)) + ' word tokens including all stopwords')
    print('\n')



# word_tokens =
# word_types =