from flask import Flask, abort, render_template, jsonify, request
from api import determine_sample_size

app = Flask('SampleSizeCalculator')

@app.route('/predict', methods=['POST'])
def do_prediction():
    if not request.json:
        abort(400)
    data = request.json

    response = determine_sample_size(data)
    print(response)
    return jsonify(response)

@app.route('/')
def index():
    return render_template('index.html')
    
app.run(debug=True)
