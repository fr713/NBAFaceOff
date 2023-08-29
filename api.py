from flask import Flask, render_template, request, jsonify
import sys  
from scoreCalculator import get_final_score

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate-scores', methods=['POST'])
def calculate_scores():
    data = request.get_json()
    player1 = data.get('player1')
    player2 = data.get('player2')
    

    result_first = get_final_score(player1)
    result_second = get_final_score(player2)
    
    return jsonify({'result1': result_first, 'result2': result_second})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
