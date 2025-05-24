from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

def create_vectorizer_and_transform(df):
    vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1,2))
    X = vectorizer.fit_transform(df['clean_message'])
    return vectorizer, X

def save_vectorizer(vectorizer, filename='vectorizer.pkl'):
    with open(filename, 'wb') as f:
        pickle.dump(vectorizer, f)