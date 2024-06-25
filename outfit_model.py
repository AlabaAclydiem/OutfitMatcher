from copy import deepcopy

from g4f.client import Client


class OutfitModel:
    def __init__(self):
        self.client = Client()
        self.messages = [
            {
                "role": "assistant",
                "content": "You're a fashion designer. Your task is to help a person choose a suitable set of clothes from the provided set, both suitable for the weather and matching colors",
            },
            {
                "role": "user",
                "content": "Clothes JSON:\n{}\nWeather JSON:\n{}\nPrevious outfit:\n{}\nPrompt:\n{} Write only suggested outfit and color coordination explanation. Do not repeat fully previous outfit. Use names from clothes JSON",
            },
        ]

    def predict(self, prompt, clothes, weather, outfit):
        messages = deepcopy(self.messages)
        messages[-1]["content"] = self.messages[-1]["content"].format(
            clothes, weather, outfit, prompt
        )
        response = self.client.chat.completions.create(
            # model="gpt-4o"
            model="gpt-3.5-turbo",
            messages=messages,
        )
        return response.choices[0].message.content

    def extract_outfit(self, prompt):
        messages = [
            {
                "role": "user",
                "content": f"Extract clothes names from this text: {prompt}. Leave only names separated by comma, NO OTHER COMMENTS",
            }
        ]
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )
        return response.choices[0].message.content
