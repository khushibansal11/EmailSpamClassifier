import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer

model=pickle.load(open('model.pkl','rb'))
vectorizer=pickle.load(open('vectorizer.pkl','rb'))

def processing(text):
    text = text.lower()  # text converted to lowercase
    text = nltk.word_tokenize(text)  # tokenized text

    # Removing special characters
    l = []
    for word in text:
        if (word.isalnum()):
            l.append(word)
    text = l[:]
    l.clear()

    # Removing stop words
    stop_words = stopwords.words('english')
    for word in text:
        if (word not in stop_words and word not in string.punctuation):
            l.append(word)

    # stemming words
    porter_stemmer = PorterStemmer()
    l = [porter_stemmer.stem(word) for word in l]

    return " ".join(l)

st.title("Email Spam Classifier")

text = st.text_area("Enter your mail")
if st.button('Check'):
    processed_text = processing(text)
    vectorized_text=vectorizer.transform([processed_text])
    prediction=model.predict(vectorized_text)[0]
    if prediction==0:
        st.header("Not Spam")
    else:
        st.header("Spam")