from flask import Flask, request, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/location', methods=['POST'])
def location():
    data = request.json
    lat = data.get("lat")
    lon = data.get("lon")

    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"\n📍 Location received at {time}")
    print(f"Latitude: {lat}")
    print(f"Longitude: {lon}")
    print(f"Map लिंक: https://www.google.com/maps?q={lat},{lon}")

    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run()
