from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
with open('knn.pkl', 'rb') as handle:
    machine_learning_model = pickle.load(handle)
print("model loaded")
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])

def predict():
    if request.method == 'POST':
        Age = int(request.form['Age'])
        Experience=int(request.form['Years'])
        Income=int(request.form['Income'])
        Family=int(request.form['Family'])
        CCAvg=float(request.form['CC'])
        Education=int(request.form['Education'])
        Mortage=int(request.form['Mortage'])
        SecuritiesAccount=int(request.form['Securities'])
        CDAccount=int(request.form['CDAccount'])
        Online=int(request.form['Banking'])
        CreditCard = int(request.form['Credit Card'])
        arr=np.array([Age,Experience,Income,Family,CCAvg,Education,Mortage,SecuritiesAccount,CDAccount,Online,CreditCard])
        arr=arr.reshape(1,11)
        prediction=machine_learning_model.predict(arr)[0]
        if prediction == np.int64(0):
            return render_template('index.html',prediction_text ="You cannot a recieve a loan")
        else:
            return render_template('index.html',prediction_text ="You can recieve a loan")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

