import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
api_url = "https://api.openai.com/v1/models"

models = requests.get(api_url, headers={'Authorization': 'Bearer ' + api_key})

models_json = json.loads(models.text)
print(json.dumps(models_json, indent=2))