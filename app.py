from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

def generate_data():
    cpu = random.randint(10, 95)
    ram = random.randint(20, 90)
    disk = random.randint(10, 80)

    # 🌱 Green Score Logic
    avg_usage = (cpu + ram + disk) / 3
    green_score = max(0, 100 - avg_usage)

    # ⚡ Optimization Suggestions
    suggestions = []

    if cpu < 20:
        suggestions.append("CPU idle → Consider shutting down instance")
    if cpu > 80:
        suggestions.append("High CPU → Scale up resources")
    if ram > 80:
        suggestions.append("High RAM usage → Optimize memory usage")

    if not suggestions:
        suggestions.append("System is running efficiently 🌱")

    return {
        "cpu_usage": cpu,
        "ram_usage": ram,
        "disk_usage": disk,
        "green_score": round(green_score, 2),
        "suggestions": suggestions
    }

@app.route('/api/data')
def get_data():
    return jsonify(generate_data())

if __name__ == '__main__':
    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=10000)
    