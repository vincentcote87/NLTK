import math
from nltk import word_tokenize
from nltk import FreqDist

def get_tf(t,d):
    count = 0
    for word in word_tokenize(d):
        if word == t:
            count = count + 1
    return 1 + math.log10(count) if count > 0 else 0


def get_word_matrix(words):
    list = []
    words = word_tokenize(words)
    for w in FreqDist(words):
        list.append(w)
    return list


def get_idf_matrix(wrd_matrix, documents, n):
    n += 0.0
    list = []
    doc_dist = []
    for d in documents:
        doc_dist.append(FreqDist(word_tokenize(d)))
    for word in wrd_matrix:
        count = 0
        for d in doc_dist:
            if d[word] > 0:
                count = count + 1
        list.append(math.log10(n/count))

    return list


def get_tf_matrix(wrd_matrix, documents):
    list = []
    for d in documents:
        doc_list = []
        for w in wrd_matrix:
            tf = get_tf(w,d)
            doc_list.append(tf)
        list.append(doc_list)
    return list


def get_w_matrix(idf_matrix, tf_matrix):
    list = []
    for d in tf_matrix:
        w_list = []
        i = 0
        n = len(idf_matrix)
        while i < n:
            w_list.append(d[i] * idf_matrix[i])
            i += 1
        list.append(w_list)
    return list


def cosine(d1,d2):
    print(len(d1))
    sum = 0.0
    i = 0
    d1d = 0.0
    d2d = 0.0
    n = len(d1)
    while i < n:
        sum += (d1[i] * d2[i])
        d1d += d1[i] * d1[i]
        d2d += d2[i] * d2[i]
        i += 1
    return (sum/(math.sqrt(d1d) * math.sqrt(d2d)))

# Bring in actual corpus
docs = ['food restaurant customer restaurant waitress', 'food store customer cashier', 'appliance store customer store cashier']
N = len(docs)
all_words = ''

for doc in docs:
    all_words = all_words + ' ' + doc


word_matrix = get_word_matrix(all_words)
idf_matrix = get_idf_matrix(word_matrix, docs, N)
tf_matrix = get_tf_matrix(word_matrix, docs)
w_matrix = get_w_matrix(idf_matrix, tf_matrix)





# print(word_matrix)
# print(idf_matrix)
# print(tf_matrix)
# print(get_w_matrix(idf_matrix, tf_matrix))
print(cosine(w_matrix[1], w_matrix[2]))


