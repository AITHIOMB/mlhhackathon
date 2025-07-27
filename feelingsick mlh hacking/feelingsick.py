G
from google import genai
client = genai.Client(api_key="gemini key")
chat = client.chats.create(model="gemini-2.5-flash")
response = chat.send_message("Symptom described: ...")
print(response.text)
