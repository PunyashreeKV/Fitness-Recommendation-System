from flask import Flask, render_template, redirect, url_for, request
from flask import request, jsonify
import pandas as pd
import numpy as np

df = pd.read_csv('fitness_exercises.csv')

app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET'])
def index():
    recommend = pd.DataFrame()
    if request.method == 'POST' and 'bodyPart' in request.form and 'target' in request.form:
        bodypart = str(request.form.get('bodyPart')).lower()
        target = str(request.form.get('target')).lower()
        recommend = df[(df.bodyPart == bodypart) & (df.target == target)]

    return render_template('index.html', lenght=len(recommend.index), recommend=recommend)

if __name__ == "__main__":
    app.run(debug=True)
