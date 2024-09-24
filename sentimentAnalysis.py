from textblob import TextBlob
import nltk
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
nltk.download('punkt_tab')
nltk.download('brown')
nltk.download('averaged_perceptron_tagger_eng')

text = "bad is bad and good is better than good"


blob = TextBlob(text)
print(blob.tags)
print(blob.noun_phrases)
print(blob.sentiment.polarity)




