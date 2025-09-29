
from flask import Flask, render_template, request, jsonify
from data import parties, compute_scores, find_closest_parties

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    scores = compute_scores(data['answers'])
    matches = find_closest_parties(scores)
    return jsonify({'scores': scores, 'matches': matches})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
