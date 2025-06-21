from flask import Flask, request, jsonify
import os

app = Flask(__name__)

notes = []

@app.route('/')
def home():
    return 'Welcome to Notes API!'

@app.route('/notes', methods=['GET'])
def get_notes():
    return jsonify(notes)

@app.route('/notes', methods=['POST'])
def add_note():
    data = request.json
    notes.append(data)
    return jsonify({'message': 'Note added!'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
