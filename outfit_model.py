from copy import deepcopy

from g4f.client import Client


class OutfitModel:
    def __init__(self):
        self.client = Client()
        self.answer_template = """
        {
            "weather_conditions": {
                "temperature": "C",
                "humidity": "%",
                "precipitation": "mm",
                "wind_speed": "m/s",
                "description": ""
            },
            "outfit_list": [
                {
                    "item": "",
                    "type": "",
                    "material": "",
                    "color": "",
                    "item_description": "",
                    "suitability_description": ""
                }
            ],
            "color_matches_from_outfit": ""
            ]
        }
        weather_conditions - base weather info
        outfit_list - a list of outfit elements
        color_matches_from_outfit - string description of outfit colors and their mathes
        """
        self.messages = [
            {
                "role": "system",
                "content": "You're a fashion designer. Your task is to help a person choose a suitable set of clothes from the provided set, both suitable for the weather and matching colors",
            },
            {
                "role": "user",
                "content": """
                    Act as fashion designer.
                    Choose stylish outfit suitable for the provided weather conditions from list of clothes in JSON format. 
                    Please do not select an outfit that has been chosen previously.
                    Here are the available outfits and weather details in JSON format:
                    Clothes JSON: {}    
                    Weather JSON: {}
                    Previous outfit: {}
                    Represent your answer strictly in JSON. Use and fill template: {} 
                    No other comments
                    """,
            },
        ]

    def predict(self, clothes, weather, outfit):
        messages = deepcopy(self.messages)
        messages[-1]["content"] = self.messages[-1]["content"].format(
            clothes, weather, outfit, self.answer_template
        )
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )
        return response.choices[0].message.content

    def extract_outfit(self, prompt):
        messages = [
            {
                "role": "user",
                "content": f"Extract all clothes items from this JSON: {prompt}, no more comments needed",
            }
        ]
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )
        return response.choices[0].message.content
