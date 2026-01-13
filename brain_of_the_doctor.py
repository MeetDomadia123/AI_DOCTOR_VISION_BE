# if you dont use pipenv uncomment the following:
# from dotenv import load_dotenv
# load_dotenv()

#Step1: Setup GROQ API key
import os

GROQ_API_KEY=os.environ.get("GROQ_API_KEY")

#Step2: Convert image to required format
import base64

def encode_image(image_path):   
    image_file=open(image_path, "rb")
    return base64.b64encode(image_file.read()).decode('utf-8')

#Step3: Setup Multimodal LLM 
from groq import Groq

# client=Groq()

# remove these eager file opens to avoid crashes on import
# image_path="acne.jpg"
# image_file=open(image_path, "rb")
# query="Is there something wrong with my face?"
model = "meta-llama/llama-4-maverick-17b-128e-instruct"
# model="meta-llama/llama-4-scout-17b-16e-instruct"
# model = "meta-llama/llama-4-scout-17b-16e-instruct"
# model="openai/gpt-oss-20b" #Deprecated

def analyze_image_with_query(query, model, encoded_image):
    client=Groq()  
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": query
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}",
                    },
                },
            ],
        }]
    chat_completion=client.chat.completions.create(
        messages=messages,
        model=model
    )

    return chat_completion.choices[0].message.content

def analyze_chat(system_prompt, history, user_text, image_filepath=None, model="meta-llama/llama-4-scout-17b-16e-instruct"):
    """
    history: list of (user, assistant) tuples
    user_text: current user turn text
    image_filepath: optional image to include this turn
    """
    client = Groq()  # uses GROQ_API_KEY from env

    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})

    for u, a in history:
        messages.append({"role": "user", "content": u})
        messages.append({"role": "assistant", "content": a})

    user_content = [{"type": "text", "text": user_text}]
    if image_filepath:
        encoded = encode_image(image_filepath)
        user_content.append({
            "type": "image_url",
            "image_url": {"url": f"data:image/jpeg;base64,{encoded}"}
        })

    messages.append({"role": "user", "content": user_content})

    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model
    )
    return chat_completion.choices[0].message.content
