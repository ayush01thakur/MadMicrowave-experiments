import os
from groq import Groq
from decouple import config


def Translation70b(sourceLanguage, targetLanguage, tone, inputText):
    groq_client = Groq(api_key=config("GROQ_API_KEY"),)
    chat_completion = groq_client.chat.completions.create(
    messages=[
            {
                "role": "system",
                "content": """You are a proficient translator and your job is to translate from given input language to output language taking the 
                given tone into consideration (just translate and add the little tone in the output language). 
                Remember to only output the translated text in the output language nothing more."""
            },
            {
                "role": "user",
                "content": f"""Input language: {sourceLanguage}, Output Language: {targetLanguage}, output tone: {tone}.
                input statement: {inputText}"""
            }
        ],
        model="llama3-70b-8192",
    )

    translatedOutput = chat_completion.choices[0].message.content
    print("funtion Completed Translation70b")

    return translatedOutput