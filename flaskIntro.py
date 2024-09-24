from flask import Flask, render_template, request, jsonify
from flask import Flask
from flask import render_template
from textblob import TextBlob
import nltk
import ssl

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('home.html')
@app.route("/analyze", methods=["POST"])
def analyze():
    text = request.json.get('text')
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

if __name__ == "__main__":
    app.run(debug=True)








