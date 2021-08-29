#Lemmatizing with NLTK

#import the stem package of nltk
from nltk.stem import WordNetLemmatizer

def lemmatize(lexUnit):
    lemmatizer = WordNetLemmatizer()
    lemmatizer.lemmatize(lexUnit)

#print the result
lemmatize("ball")
