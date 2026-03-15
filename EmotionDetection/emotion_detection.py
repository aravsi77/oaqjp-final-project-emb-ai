import requests
import json

#function to realize the emotion detection 
def emotion_detector(text_to_analyze):
    #get the date from IBM watson API
    url =  'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input =  { "raw_document": { "text": text_to_analyze } }
    #send the request to ibm Watson and get the response
    response = requests.post(url, json = input, headers = header)
    #check the status code
    status_code = response.status_code
    #check status code 400 (empty string)
    if status_code == 400:
        empty_dict = {'anger':None,'disgust':None,'fear':None,'joy':None,'sadness':None,'dominant_emotion':None}
        return empty_dict
    #format the response to text
    formatted_response = json.loads(response.text)
    #get only the emotion response and store them in a dictionary
    emotions_dict = formatted_response['emotionPredictions'][0]['emotion']
    #extract the key and value to the list
    emotions = list(emotions_dict.keys())
    score = list(emotions_dict.values())
    #search for dominant emotion
    max_score = max(score)
    dominant_emotion = emotions[score.index(max_score)]
    #update the emotion dictionary to add the dominant
    emotions_dict['dominant_emotion'] = dominant_emotion
    #return the response
    return emotions_dict

