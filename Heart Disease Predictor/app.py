import flask; print(flask.__version__)
from flask import Flask, render_template, request
import os
import numpy as np
import pickle

app = Flask(__name__)
app.env = "development"
result = ""
print("I am in flask app")

@app.route('/', methods=['GET'])
def hello():
    print("I am In hello. Made some changes")
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    print("Request.method:", request.method)
    print("Request.TYPE", type(request))
    print("In the process of making a prediction.")
    if request.method == 'POST':
        print(request.form)
        age = request.form['age']
        sex = request.form['sex']
        Cp = request.form['Cp']
        trestbps = request.form['trestbps']
        Cholestrol = request.form['Cholestrol']
        fbs= request.form['fbs']
        restecg = request.form['restecg']
        thalach = request.form['thalach']
        exang = request.form['exang']
        oldpeak = request.form['oldpeak']
        slope = request.form['slope']
        ca = request.form['ca']
        thal = request.form['thal']
        print(age, sex, Cp,trestbps,Cholestrol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
        test_arr =[[age, sex, Cp,trestbps,Cholestrol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]]
        model = pickle.load(open('ml_model.pkl', 'rb'))
        print("Model Object: ", model)
        prediction = model.predict(test_arr)
        predicted = "Yes" if prediction else "No" 
        result = f"The model has predicted : {predicted}"
        return render_template('index.html', result=result)
    return render_template('index.html')

app.run(host='0.0.0.0', port=5001, debug=True)