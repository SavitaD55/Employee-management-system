from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# MongoDB connection
client = MongoClient("mongodb://127.0.0.1:27017/")
db = client["companyDB"]
collection = db["employees"]

# Add employee
@app.route('/add', methods=['POST'])
def add_employee():
    data = request.get_json()
    collection.insert_one(data)
    return jsonify({"message": "Employee added successfully"})

# Get employees
@app.route('/get', methods=['GET'])
def get_employees():
    employees = []
    for emp in collection.find():
        emp["_id"] = str(emp["_id"])  # convert ObjectId to string
        employees.append(emp)
    return jsonify(employees)

# Run app
if __name__ == '__main__':
    app.run(debug=False,
use_reloader=False)