import os
from groq import Groq
from decouple import config


def Translation70b(sourceLanguage, targetLanguage, tone, inputText):
    groq_client = Groq(api_key=config("GROQ_API_KEY"),)
    chat_completion = groq_client.chat.completions.create(
    messages=[
            {
                "role": "system",
                "content": """You are a proficient translator and your job is to translate the given input text 
                from input language to given output language taking the given tone and actual meaning into consideration 
                (just translate and add the little tone and dont change the meaning in the output language and give output only in output language). 
                Recognize the idioms and converstional gestures/tone and then give the natural translations. 
                Remember to only output the translated text in the output language and nothing more (If input Text is an url leave the url as it is)."""
            },
            {
                "role": "user",
                "content": f"""Input language: {sourceLanguage}, Output Language: {targetLanguage}, output tone: {tone},
                input text: {inputText}"""
            }
        ],
        model="llama3-70b-8192",
    )

    translatedOutput = chat_completion.choices[0].message.content
    print("funtion Completed Translation70b: ", translatedOutput)

    return translatedOutput