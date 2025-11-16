from flask import Flask, request, jsonify
import psycopg2
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

DB_HOST = "db"
DB_NAME = "mydb"
DB_USER = "admin"
DB_PASS = "secret"

def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

@app.route("/save", methods=["POST"])
def save_name():
    data = request.json
    name = data.get("name")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name) VALUES (%s)", (name,))
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"message": f"{name} saved!"})

@app.route("/names", methods=["GET"])
def get_names():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT name FROM users")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    names = [row[0] for row in rows]
    return jsonify({"names": names})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

