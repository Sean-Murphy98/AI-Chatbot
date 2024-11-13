import requests

API_URL = "https://api-inference.huggingface.co/models/EleutherAI/gpt-neo-2.7B"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	print(payload)
	print(response.json())
	return response.json()
	
output = query({
	"inputs": "Can you please let us know more details about your boobs",
})