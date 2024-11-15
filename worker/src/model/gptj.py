import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

class GPT:
    def __init__(self):
        self.url = os.environ.get('MODEL_URL')
        self.headers = {
            "Authorization": f"Bearer {os.environ.get('HUGGINFACE_INFERENCE_TOKEN')}"}
        self.payload = {
            "inputs": "",
            "parameters": {
                "return_full_text": False,
                "use_cache": True,
                "max_new_tokens": 25
            }
        }

    def query(self, input: str) -> list:
        self.payload["inputs"] = f"Human: {input} Bot:"
        response = requests.post(self.url,headers=self.headers,json=self.payload)
        data = json.loads(response.content.decode("utf-8"))
        text = data[0]['generated_text']
        res = str(text).strip("\n").strip()
        print(res)
        return res

if __name__ == "__main__":
    GPT().query("Will artificial intelligence help humanity conquer the universe?")