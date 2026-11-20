from flask import Flask, render_template, request
from EmotionDetection import emotion_detection as ed

"""
Flask environment for Emotion Detection
"""

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detector():
    """
    Computes emotion detection
    """
    txt = request.args.get('textToAnalyze')
    return ed.emotion_detector(txt)

@app.route("/")
def render_index_page():
    """
    Default page
    """
    return render_template('index.html')

if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=5000)
    #app.run(port=5000,debug=True)
    app.run(debug=True)
