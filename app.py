from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Age = int(request.form['Age'])
        Gender=request.form['Gender']
        if(Gender=='Male'):
            Sex=1
        else:
            Sex=0
        Bmi=float(request.form['Bmi'])
        Children=int(request.form['Children'])
        Smoker=request.form['Smoker']
        if(Smoker=='yes'):
            Smoker_f=1
        else:
            Smoker_f=0
        prediction=model.predict([[Age,Sex,Bmi,Children,Smoker_f]])
        output=prediction[0]
        return render_template("index.html",prediction_text="The insurance coast prediction is {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

