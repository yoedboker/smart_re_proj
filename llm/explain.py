# This file serves as the OpenAI LLM client for generating natural-language explanations.

import openai

class LLMExplain:
    def __init__(self, api_key):
        openai.api_key = api_key

    def explain(self, prompt):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content']