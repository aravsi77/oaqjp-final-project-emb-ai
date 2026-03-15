'''This module run the server'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
#Initiate the flask app
app = Flask("Emotion Detector")

@app.route('/emotionDetector')
def sent_detector():
    '''capture the text from html file'''
    text_to_analyze = request.args.get('textToAnalyze')
    resp = emotion_detector(text_to_analyze)
    #check if dictionary contains none
    if resp['anger'] is None:
        return "Invalid text! Please try again"
    return (
        f"For the given statement, the system response is 'anger': {resp['anger']}, "
        f"'disgust': {resp['disgust']}, 'fear': {resp['fear']}, 'joy': {resp['joy']}, "
        f"'sadness': {resp['sadness']}. The dominant emotion is {resp['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    '''render static index html'''
    return render_template('index.html')


if __name__ == "__main__":
    #This functions executes the flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0", port=5000)
