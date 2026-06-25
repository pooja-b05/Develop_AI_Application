"App file"

from flask import Flask, render_template, request, jsonify

from emotion_detector import analyze_emotion

app = Flask(__name__)


@app.route("/")
def home():
    """Home"""
    return render_template("index.html")


@app.route("/emotion", methods=["POST"])
def emotion():
    """Emotion"""
    text = request.form.get("text")

    result = analyze_emotion(text)

    if result.get("error"):
        return jsonify({"error": result["error"]})

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
