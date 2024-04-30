from flask import Flask, request, render_template
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # 允许跨域请求

@app.route('/')
def index():
    return render_template('location.html')

@app.route('/location', methods=['POST'])
def receive_location():
    data = request.json
    print('Received latitude:', data['latitude'])
    print('Received longitude:', data['longitude'])
    return 'Location received'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
