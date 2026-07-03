from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/api/status")
def status():
    return jsonify({"status": "WF7 OK", "engine": "super"})

@app.route("/api/modules")
def modules():
    mods = []
    for root, dirs, files in os.walk("/opt/wf7/pro_engine"):
        for f in files:
            mods.append(f)
    return jsonify({"modules": mods})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7070)
