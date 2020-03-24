from gensim.models import Word2Vec
from nltk.corpus import brown

cat = 'news'
# cat = 'editorial'
# cat = 'reviews'
# cat = 'religion'
# cat = 'hobbies'
# cat = 'lore'
# cat = 'belle_lettres'
# cat = 'government'
# cat = 'learned'
# cat = 'fiction'
# cat = 'mystery'
# cat = 'science_fiction'
# cat = 'adventrue'
# cat = 'romance'
# cat = 'humor'

# cat2 = 'news'
cat2 = 'editorial'
# cat2 = 'reviews'
# cat2 = 'religion'
# cat2 = 'hobbies'
# cat2 = 'lore'
# cat2 = 'belle_lettres'
# cat2 = 'government'
# cat2 = 'learned'
# cat2 = 'fiction'
# cat2 = 'mystery'
# cat2 = 'science_fiction'
# cat2 = 'adventrue'
# cat2 = 'romance'
# cat2 = 'humor'

# docs = []
# docs.append(brown.words(categories=cat))
# docs.append(brown.words(categories=cat2))

doc1 = Word2Vec(brown.words(categories=cat))

print(len(brown.words(categories=cat)))

print(len(doc1.wv.syn0))

# Don't know how to do this...