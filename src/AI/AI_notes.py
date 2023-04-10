"""
CS399 Aritificial Intelligence

"""

"""
Large Language Models

Representing words as vectors

*** Dimensions ***
working in 300 dimensional space

*** Word Embeddings ***
one-hot encoded vector
each word is represented by a unique vector 

*** Deistributed Represnetation ***
distrubutes information over all dimentions available
fitting 50000 words into 300 dimensions
Now each word is represnted not by a unique combination of values in each dimension

similar words occur together and have similar context
similar words might have same or similar values i particular vectors that define them

training phase uses the "context" of each word to group them as similar

*** Training ***
CBOW: Continuous Bag of words

Skip Gram: given a target word and predict the context

with the context words dound togeterh in the training samples are pired together which gives them more context together

"""

"""
Manhattan Distance: magnitude of a vector as an approximation

Euclidean Distance: A more direct magnitude literal magnitude od a vector ex sqrt(x1^2 + x2^2)





"""

