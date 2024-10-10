import requests 

import requests

import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers = headers)
    res = json.loads(response.text)
    formatted_output = res['emotionPredictions'][0]['emotion']
    formatted_response = {
        'anger': formatted_output.get('anger', 0.0),
        'disgust': formatted_output.get('disgust', 0.0),
        'fear': formatted_output.get('fear', 0.0),
        'joy': formatted_output.get('joy', 0.0),
        'sadness': formatted_output.get('sadness', 0.0)
    }
        
    dominant_emotion = max(formatted_output, key=formatted_output.get)
    
    formatted_response['dominant_emotion'] = dominant_emotion
    return formatted_response
