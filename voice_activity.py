import requests
import base64

url = "https://proxy.api.deepaffects.com/audio/generic/api/v1/async/vad"

querystring = {"apikey":"<API_KEY>", "webhook":"<WEBHOOK_URL>"}

payload = {
    "encoding": "Wave",
    "languageCode": "en-US",
    "minNonSpeechDuration": 1
}

# The api accepts data either as a url or as base64 encoded content
# passing payload as content:
with open(audio_file_name, 'rb') as fin:
    audio_content = fin.read()
payload["content"] = base64.b64encode(audio_content).decode('utf-8')

headers = {
    'Content-Type': "application/json",
}

response = requests.post(url, json=payload, headers=headers, params=querystring)

print(response.text)
