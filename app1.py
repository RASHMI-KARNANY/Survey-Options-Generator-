import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
# model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index2.html')

@app.route('/predict',methods=['POST'])
def predict():
    inputted_string=request.form["question"]
    # int_features = [int(x) for x in request.form.values()]
    # final_features = [np.array(int_features)]
    if inputted_string.startswith("is") or inputted_string.startswith("do"):
        output = "Yes or no"
    elif inputted_string.startswith("how") or inputted_string.startswith("where") or inputted_string.startswith("why"):
        output = "text field"
    elif "how much" in inputted_string: 
        output = "range"
    else:
        output = "other"
    
    # prediction = model.predict(final_features)
    # output = round(prediction[0], 2)
    return render_template('index2.html', prediction_text=' Prediction is {}'.format(output))

# @app.route('/results',methods=['POST'])
# def results():

#     data = request.get_json(force=True)
#     prediction = model.predict([np.array(list(data.values()))])

#     output = prediction[0]
#     return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)