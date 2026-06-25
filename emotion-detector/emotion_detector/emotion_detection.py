"Emotion detection file"
import requests


def analyze_emotion(text):
    """
    Analyze emotions using Watson NLP
    """
    if not text:
        return {
            "emotion": None,
            "error": "No text provided"
        }

    url = ("https://api.us-south.natural-language-understanding.watson.cloud.ibm.com"
           "/instances/YOUR_INSTANCE/v1/analyze?version=2021-08-01")

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "text": text,
        "features": {
            "emotion": {}
        }
    }

    try:
        response = requests.post(
            url,
            json=payload,
            auth=("apikey", "YOUR_API_KEY"),
            headers=headers,
            timeout=30
        )

        result = response.json()

        emotions = result["emotion"]["document"]["emotion"]

        dominant_emotion = max(emotions, key=emotions.get)

        return {
            "anger": emotions["anger"],
            "disgust": emotions["disgust"],
            "fear": emotions["fear"],
            "joy": emotions["joy"],
            "sadness": emotions["sadness"],
            "dominant_emotion": dominant_emotion
        }

    except Exception as e:
        return {
            "error": str(e)
        }
