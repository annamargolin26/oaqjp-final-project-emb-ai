import requests
import json

"""
Emotion  Detection utilities
"""
def emotion_detector(text_to_analyze):
    """
    Gets EmotionDetection
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the sentiment analysis service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    input_json = { "raw_document": { "text": text_to_analyze } }  # Create a dictionary with the text to be analyzed
    response = requests.post(url, json = input_json, headers=header)  # Send a POST request to the API with the text and headers
    json_response = json.loads(response.text)
    dict=json_response["emotionPredictions"][0]["emotion"]

    max_key=None
    max_value=0.0
    for key,value in dict.items():
        if value > max_value:
            max_value=value
            max_key=key
    
    dict['dominant_emotion']=max_key 
    return dict
