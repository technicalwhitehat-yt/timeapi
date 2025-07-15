from flask import Flask, jsonify
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route("/")
def get_time():
    now = datetime.now(pytz.timezone("Asia/Kolkata"))
    return jsonify({
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M:%S"),
        "datetime": now.isoformat()
    })

if __name__ == "__main__":
    app.run()
