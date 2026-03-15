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
    #format the response to text
    formatted_response = json.loads(response.text)
    #return the response
    return formatted_response

