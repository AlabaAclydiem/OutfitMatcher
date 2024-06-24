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
                "content": "Clothes JSON:\n{}\nWeather JSON:\n{}\nPrompt:\n{} Write only suggested outfit and color coordination explanation",
            },
        ]
        self.model = "gpt-4o"

    def predict(self, prompt, clothes, weather):
        self.messages[-1]["content"] = self.messages[-1]["content"].format(
            clothes, weather, prompt
        )
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages,
        )
        return response.choices[0].message.content
