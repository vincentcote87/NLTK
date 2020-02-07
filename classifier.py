# CPSC4310 Assignment #2 Question 4
# By Vincent Cote

from nltk.corpus import stopwords
from nltk.corpus import brown
from nltk.probability import FreqDist
# from nltk import NaiveBayesClassifier, classify
from random import shuffle
from math import floor


documents = [(list(brown.words(fileid)), category) for category in brown.categories() for fileid in brown.fileids(category)]
shuffle(documents)

training_set = documents[:350]
testing_set = documents[350:]

def p(x,c):
    for sets in range(len(training_set)):
        if training_set[sets][1] == 

for x in range(len(training_set)):
    print(training_set[x][1])



# stop_words = set(stopwords.words('english'))
# punctuation = set({'.', '!', '?', ';', ',', '\'\'', '(', ')', '``', '--', ':'})
# # categories = brown.categories()

# def filter_text(word_list):
#     new_list = []
#     for w in word_list:
#         if w.lower() not in stop_words and w not in punctuation:
#             new_list.append(w)
#     return new_list

# documents = []
# for category in brown.categories():
#     types = FreqDist(filter_text(brown.words(categories=category)))
#     temp_list = [category]
#     temp_list.append(types)
#     documents.append(temp_list)

# all_words = FreqDist(filter_text(brown.words()))

# def p(feature, c):

# def filter_text(word_list):
#     new_list = []
#     for w in word_list:
#         if w.lower() not in stop_words and w not in punctuation:
#             new_list.append(w)
#     return new_list

# documents = []
# for category in brown.categories():
#     temp_list = []
#     for word in brown.words(categories=category):
#         if word.lower() not in stop_words and word not in punctuation:
#             temp_list.append(word)
#     documents.append((temp_list, category))



# documents = [(list(brown.words(fileid)), category) for category in brown.categories() for fileid in brown.fileids(category)]

# shuffle(documents)

# all_words = []
# for word in brown.words():
#     if word.lower() not in stop_words and word not in punctuation:
#         all_words.append(word.lower())

# all_words = FreqDist(all_words)

# word_features = list(all_words.keys())[:3000]

# def find_features(document):
#     words = set(document)
#     features = {}
#     for w in word_features:
#         features['contains(%s)' % w] = (w in words)
#     return features

# feature_set = [(find_features(doc), category) for (doc, category) in documents]

# training_set = feature_set[:2000]
# testing_set = feature_set[2000:]

# classifier = NaiveBayesClassifier.train(training_set)
# print('accuracy: ', (classify.accuracy(classifier, testing_set) * 100))
# classifier.show_most_informative_features(15)




# trainingData = []
# for category in brown.categories():
#     types = FreqDist(filter_text(brown.words(categories=category)))
#     temp_list = [category]
#     temp_list.append(types)
#     trainingData.append(temp_list)

# # for (x, y) in trainingData[0][1]:
# #     print(x + " " + y)

# print(trainingData[0][1])


# trainingData = []
# for cat in categories:
#     sentences = brown.sents(categories=cat)
#     # Only taking 70% of the sentences
#     for i in range(floor(len(sentences) * 0.7)):
#         temp_list = [cat]
#         temp_list.append(filter_text(sentences[i]))
#         trainingData.append(temp_list)

# print(trainingData[1])

