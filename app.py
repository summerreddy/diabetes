
from flask import Flask,request, url_for, redirect, render_template
import pickle
import pandas as pd

app = Flask(__name__)

model = pickle.load(open("Diabetes.pkl", "rb"))


@app.route('/')
def  home():
    return render_template("index.html")
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        preg = int(request.form['pregnancies'])
        glucose = int(request.form['glucose'])
        bp = int(request.form['bloodpressure'])
        st = int(request.form['skinthickness'])
        insulin = int(request.form['insulin'])
        bmi = float(request.form['bmi'])
        dpf = float(request.form['dpf'])
        age = int(request.form['age'])
    row_df = pd.DataFrame([pd.Series([preg, glucose, bp, st, insulin, bmi, dpf, age])])

    print(row_df)
    my_prediction=model.predict(row_df)
    print(my_prediction)    
    if my_prediction == 1:
            pred = "You have Diabetes, please consult a Doctor."
    elif my_prediction == 0:
        pred = "You don't have Diabetes."
    output = pred
    return render_template('result.html', prediction_text='{}'.format(output))      
if __name__ == '__main__':
    app.run(debug=True)
