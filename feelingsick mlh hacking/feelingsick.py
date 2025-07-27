
from google import genai
client = genai.Client(api_key="AIzaSyDTzd5cIjS2ExSR80UFtgNfUjp7gro3v0U")
chat = client.chats.create(model="gemini-2.5-flash")
response = chat.send_message("Symptom described: ...")
print(response.text)
