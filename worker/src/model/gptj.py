import os
from dotenv import load_dotenv
import requests
import json
from ..redis.config import Redis
from ..schema.chat import Message

load_dotenv()
redis = Redis()

class GPT:
    def __init__(self):
        self.url = os.environ.get('MODEL_URL')
        self.headers = {
            "Authorization": f"Bearer {os.environ.get('HUGGINFACE_INFERENCE_TOKEN')}"}
        self.payload = {
            "inputs": "",
            "parameters": {
                "return_full_text": False,
                "use_cache": False,
                "max_new_tokens": 25
            }

        }
        self.json_client = redis.create_rejson_connection()
        redis_client = redis.create_connection()

    def query(self, input: str) -> list:
        self.payload["inputs"] = f"{input} Bot:"
        print(self.payload)
        response = requests.post(self.url, headers=self.headers, json=self.payload)
        
        data = json.loads(response.content.decode("utf-8"))
        text = data[0]['generated_text']

        res = str(text.split("Human:")[0]).strip("\n").strip()
        print(self.payload)
        return res

if __name__ == "__main__":
    GPT().query("Will artificial intelligence help humanity conquer the universe?")