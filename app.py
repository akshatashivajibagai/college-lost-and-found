from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

DB_FILE = "data.json"

def load_db():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, 'r') as f:
        return json.load(f)

def save_db(data):
    with open(DB_FILE, 'w') as f:
        json.dump(data, f, indent=2)

@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(load_db())

@app.route('/api/items', methods=['POST'])
def add_item():
    data = load_db()
    new_item = request.json
    data.append(new_item)
    save_db(data)
    return jsonify({"success": True})

if __name__ == '__main__':
   import os
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)