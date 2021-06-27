from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re
from nltk.stem import PorterStemmer



def tokenizer(txt):
   ## returns tokenized corpus without stopwords and special characters
    
    ##parameter: 
    ##txt: string
    ps = PorterStemmer()
    stop_words = set(stopwords.words('english')) 
    txt = re.sub('[^A-Za-z\s*]', '', txt.lower())
    tokens = list(filter(lambda x: x not in stop_words and len(x) > 2, word_tokenize(txt)))
    return tokens
    #return list([ps.stem(token) for token in tokens]) 