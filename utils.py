import requests
import json
from .config import Config

config = Config()  # Assuming Config class to load from config.json

def make_api_request(text):
    headers = {
        'Authorization': f'Bearer {config.api_key}',
        'Content-Type': 'application/json'
    }
    data = {
        'text': text
    }
    response = requests.post(config.api_endpoint, headers=headers, json=data)
    return response.json()

def preprocess_text(text):
    # Implement text preprocessing logic here if needed
    return text

