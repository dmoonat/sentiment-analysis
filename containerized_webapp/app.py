from flask import Flask,render_template,url_for,request
import pandas as pd 
import numpy as np
from nltk.stem.porter import PorterStemmer
import re
import string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

app = Flask(__name__)

def remove_pattern(input_txt,pattern):
    '''
    removes pattern from input_txt using regex
    '''
    r = re.findall(pattern,input_txt)
    for i in r:
        input_txt = re.sub(i,'',input_txt)

    ## removes punctuations
    input_txt = re.sub(r'[^\w\s]', ' ', input_txt)

    return input_txt.strip().lower()


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        clean_test = remove_pattern(message,"@[\w]*")
        tokenized_clean_test = clean_test.split()
        stem_tokenized_clean_test = [stemmer.stem(i) for i in tokenized_clean_test]
        message = ' '.join(stem_tokenized_clean_test)
        data = [message]
        data = cv.transform(data)
        my_prediction = clf.predict(data)
    return render_template('result.html',prediction = my_prediction)


if __name__ == '__main__':
	
	##initialize stemmer	
	stemmer = PorterStemmer()

	##load vectorizer and model
	with open('model/logistic_clf.pkl', 'rb') as f:
	    cv, clf = pickle.load(f)
	
	app.run(host='0.0.0.0',port=5000)
