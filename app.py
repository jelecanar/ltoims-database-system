from flask import Flask, jsonify, request
import mariadb
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_connection():
    return mariadb.connect(
        host="localhost",
        user="root",
        password="yourpassword",
        database="JimlethDB"
    )

@app.route("/")
def home():
    return jsonify({"message": "JimlethDB Backend is running"})

@app.route("/drivers")
def get_drivers():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM driver")
    drivers = cursor.fetchall()

    conn.close()
    return jsonify(drivers)

@app.route("/vehicles")
def get_vehicles():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM vehicle")
    vehicles = cursor.fetchall()

    conn.close()
    return jsonify(vehicles)

@app.route("/violations")
def get_violations():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM traffic_violation")
    violations = cursor.fetchall()

    conn.close()
    return jsonify(violations)

@app.route("/registrations")
def get_registrations():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM vehicle_registration")
    registrations = cursor.fetchall()

    conn.close()
    return jsonify(registrations)

if __name__ == "__main__":
    app.run(debug=True)
