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
    d = ed.emotion_detector(txt)

    if d['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    result = "For the given statement, the system response is "
    count = 0
    total = len(d)

    for key, value in d.items():
        if key != "dominant_emotion":
            result = f"{result}'{key}': {value}"
            count += 1
            if count == (total - 2):
                result = f"{result} and "
            elif count == (total - 1):
                result = f"{result}. "
            else:
                result = f"{result}, "

    result = f"{result}The dominant emotion is {d['dominant_emotion']}."
    return result

@app.route("/")
def render_index_page():
    """
    Default page
    """
    return render_template('index.html')

if __name__ == "__main__":
     app.run(host="127.0.0.1",port=5000,debug=True)
