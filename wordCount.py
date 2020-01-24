from nltk.corpus import stopwords
from nltk.corpus import brown
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.probability import FreqDist


lemmatizer = WordNetLemmatizer()
ps = PorterStemmer()

stop_words = set(stopwords.words('english'))
punctuation = set({'.', '!', '?', ';', ',', '\'\'', '(', ')', '``', '--', ':'})
all_words = brown.words()

def filter_text(word_list, lemmatized=False, stemmed=False):
    new_list = []
    for w in word_list:
        if w.lower() not in stop_words and w not in punctuation:
            if lemmatized:
                new_list.append(lemmatizer.lemmatize(w))
            elif stemmed:
                new_list.append(ps.stem(w))
            else:
                new_list.append(w)
    return new_list

def promptUser():
    return input(
            "Options:\n1)With stopwords\n2)Without stopwords\n3)Without stopwords and lemmatization\n4)Without stopwords and stemming\n" +
            "Please choose an mode: "
            )

while True:
    mode = promptUser()
    if mode == '1' or mode == '2' or mode == '3' or mode == '4':
        break

for category in brown.categories():
    words_in_category = brown.words(categories=category)
    if mode == '1':
        filtered_text = words_in_category
    else:
        filtered_text = filter_text(words_in_category, mode == '3', mode == '4')

    types = FreqDist(filtered_text)

    print('****************************** ' + category + ' ******************************')
    print(' -This category has ' + str(len(words_in_category)) + ' word tokens')
    print(' -This category has ' + str(len(types)) + ' word types')
    print(' -The top 5 most common words are :\n')
    print(types.most_common(5))
    print('\n')

print('And the size of the total vocabulary is ' + str(len(FreqDist(all_words))))
