from flask import Flask, render_template, request, jsonify
from datetime import datetime

from ai.hook import generate_hook
from ai.script import generate_script
from ai.scenes import generate_scenes
from ai.cta import generate_cta

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

def validate(data):
    required = ["product", "description", "audience", "goal"]

    missing = [field for field in required if not data.get(field)]

    if missing:
        return False, missing

    return True, None

@app.route("/api/hook", methods=["POST"])
def hook():

    data = request.json

    valid, missing = validate(data)

    if not valid:
        return jsonify({
            "error": f"Missing required fields: {', '.join(missing)}"
        }), 400

    result = generate_hook(
        data["product"],
        data["audience"]
    )

    return jsonify({
        "hook": result,
        "timestamp": datetime.utcnow().isoformat()
    })

@app.route("/api/script", methods=["POST"])
def script():

    data = request.json

    valid, missing = validate(data)

    if not valid:
        return jsonify({
            "error": f"Missing required fields: {', '.join(missing)}"
        }), 400

    result = generate_script(
        data["product"],
        data["audience"],
        data["goal"],
        data.get("duration", 30)
    )

    return jsonify({
        "script": result,
        "timestamp": datetime.utcnow().isoformat()
    })

@app.route("/api/scenes", methods=["POST"])
def scenes():

    data = request.json

    valid, missing = validate(data)

    if not valid:
        return jsonify({
            "error": f"Missing required fields: {', '.join(missing)}"
        }), 400

    result = generate_scenes(
        data["product"],
        data["goal"]
    )

    return jsonify({
        "scenes": result,
        "timestamp": datetime.utcnow().isoformat()
    })

@app.route("/api/cta", methods=["POST"])
def cta():

    data = request.json

    valid, missing = validate(data)

    if not valid:
        return jsonify({
            "error": f"Missing required fields: {', '.join(missing)}"
        }), 400

    result = generate_cta(
        data["product"],
        data["audience"],
        data["goal"]
    )

    return jsonify({
        "cta": result,
        "timestamp": datetime.utcnow().isoformat()
    })

@app.route("/api/generate-all", methods=["POST"])
def generate_all():

    data = request.json

    valid, missing = validate(data)

    if not valid:
        return jsonify({
            "error": f"Missing required fields: {', '.join(missing)}"
        }), 400

    duration = data.get("duration", 30)

    return jsonify({
        "hook": generate_hook(
            data["product"],
            data["audience"]
        ),
        "script": generate_script(
            data["product"],
            data["audience"],
            data["goal"],
            duration
        ),
        "scenes": generate_scenes(
            data["product"],
            data["goal"]
        ),
        "cta": generate_cta(
            data["product"],
            data["audience"],
            data["goal"]
        ),
        "timestamp": datetime.utcnow().isoformat()
    })

if __name__ == "__main__":
    app.run(debug=True)