# map-emotions-to-eye-movement
# description: generate sequence of eye state for each character for the length/duration of the animation
# side task: how do we discover non speech sounds in audio e.g 


#identify the emotion and how long that emotion takes
# import eyes and lids and generate sequence from them
# from deepaffects.realtime.util import chunk_generator_from_file, chunk_generator_from_url, get_deepaffects_client
from emotion_utils import Is_sad, Is_joy, Is_neutral

import requests
import base64

sync_url = "https://proxy.api.deepaffects.com/audio/generic/api/v2/sync/recognise_emotion" # sync api url

querystring = {"apikey":"<API_KEY>"}

payload = {
    "encoding": "Wave",
    "languageCode": "en-US"
}

# passing payload as content:
with open(audio_file_name, 'rb') as fin:
    audio_content = fin.read()
payload["content"] = base64.b64encode(audio_content).decode('utf-8')

headers = {
    'Content-Type': "application/json",
}


# alternatively use sync request for payload upto 1 minute
response = requests.post(sync_url, json=payload, headers=headers, params=querystring)

print(response.text)
# [
#     {
#         "emotion": "joy",
#         "start": 0.0,
#         "end": 3.0
#     },{
#         "emotion": "neutral",
#         "start": 3.0,
#         "end": 6.0
#     }
# ]

def iteration(response):
        for emotion_dict in response.text:
            #  {
            #     "emotion": "joy",
            #     "start": 0.0,
            #     "end": 3.0
            #  }
            for key,val in emotion_dict.items():
                while emotion_dict[key] == "emotion":
                    if emotion_dict[val] == 'sadness':
                        Is_sad()
                    if emotion_dict[val]== 'joy':
                        Is_joy()
                    else:
                        Is_neutral()