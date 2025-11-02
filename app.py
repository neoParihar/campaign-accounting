from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Configure MySQL connection
db_config = {
    "user": "root",
    "password": "password",
    "host": "127.0.0.1",  # Host is localhost since Flask runs outside Docker
    "database": "campaignFunds_db",
}


@app.route("/")
def index():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT NOW();")
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return jsonify({"server_time": result[0].isoformat()})


if __name__ == "__main__":
    app.run(debug=True)
