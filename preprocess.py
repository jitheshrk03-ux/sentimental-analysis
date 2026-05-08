import nltk
nltk.download('stopwords',quite=True)
nltk.download('wordnet',quite=True)
nltk.download('punkt',quite=True)
nltk.download('punk_tab')
from nltk.corpus import movie_reviews,stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import re
stop_words=stopwords.words('english')
lemmatizer=WordNetLemmatizer()
len(stop_words)
stop_words
lemmatizer.lemmatize("better",pos='v')
def preprocess(text):
  # convert text into lowercase
  text=text.lower()

  # remove punctuation,numbers from the text
  text=re.sub('[^a-zA-Z]',' ',text)

  #Tokenize: Convert text into list of words
  tokens=word_tokenize(text)

  #Remove stopwords and apply lemmatization
  tokens=[token for token in tokens if token not in stop_words]

  #Lemmatize each token: convert words into its root from
  lemmatize_tokens=[lemmatizer.lemmatize(token) for token in tokens]

  return " ".join(lemmatize_tokens) #converting back to the text format
print(preprocess('The Movie is really amazing!!'))
