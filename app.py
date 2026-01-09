from flask import Flask, render_template, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

def detect_emotion(text):
    polarity = TextBlob(text).sentiment.polarity

    if polarity < -0.4:
        return "Frustrated"
    elif polarity < 0:
        return "Confused"
    elif polarity > 0.4:
        return "Confident"
    else:
        return "Neutral"

def confusion_level(text):
    length = len(text.split())
    if length < 5:
        return "Low"
    elif length < 15:
        return "Medium"
    else:
        return "High"

def generate_solution(emotion, confusion):
    if emotion in ["Frustrated", "Confused"] and confusion == "High":
        return "Take a deep breath 🙂 Let's break this into small steps and solve it slowly."
    elif confusion == "Medium":
        return "You're almost there 👍 Here's a clearer explanation with an example."
    else:
        return "Great! Here's a concise and advanced explanation."

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    text = data.get("text")

    emotion = detect_emotion(text)
    confusion = confusion_level(text)
    solution = generate_solution(emotion, confusion)

    return jsonify({
        "emotion": emotion,
        "confusion": confusion,
        "solution": solution
    })

if __name__ == "__main__":
    app.run(debug=True)
