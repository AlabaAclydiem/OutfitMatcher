from copy import deepcopy

from g4f.client import Client


class OutfitModel:
    def __init__(self):
        self.client = Client()
        self.answer_template = """
        {
            'weather_conditions': {
                'temperature': 'C',
                'humidity': '%',
                'precipitation': 'mm',
                'wind_speed': 'm/s',
                'description': ''
            },
            'outfit_list': [
                {
                    'item': '',
                    'type': '',
                    'material': '',
                    'color': '',
                    'item_description': '',
                    'suitability_description': ''
                }
            ],
            'color_matches_from_outfit': ''
        }
        weather_conditions: base weather info
        outfit_list: a list of outfit elements
        color_matches_from_outfit: string description of outfit colors and their mathes
        """
        self.main_content = """
        Act as fashion designer.
        Choose stylish outfit suitable for the provided weather conditions from list of clothes in JSON format. 
        Please do not select an outfit that has been chosen previously.
        Here are the available outfits and weather details in JSON format:
        Clothes JSON: {}    
        Weather JSON: {}
        {}
        Previous outfit: {}
        Represent your answer strictly in JSON. Use and fill template: {} 
        No other comments
        """
        self.example = """
        Here's an example for you:
        {
            'weather_conditions': {
                'temperature': '13 C',
                'humidity': '45%',
                'precipitation': '123 mm',
                'wind_speed': '2.3 m/s',
                'description': 'The weather is currently mild, with moderate humidity and precipitation. The wind is blowing at a moderate speed.'
            },
            'outfit_list': [
                {
                    'item': 'Jacket',
                    'type': 'Upperwear',
                    'material': 'Polyester',
                    'color': 'Black',
                    'item_description': 'A warm and water-resistant black polyester jacket.',
                    'suitability_description': Suitable for the mild temperature and high precipitation, providing warmth and protection from rain.'
                },
                {
                    'item': 'T-Short',
                    'type': 'Body',
                    'material': 'Silk',
                    'color': 'Light Blue',
                    'item_description': 'A light blue silk T-shirt that is comfortable and breathable.',
                    'suitability_description': 'Comfortable for mild weather, though might not be ideal in high humidity and precipitation unless worn under the jacket.'
                },
                {
                    'item': 'Jeans',
                    'type': 'Legs',
                    'material': 'Denim',
                    'color': 'Blue',
                    'item_description': 'Classic blue denim jeans.',
                    'suitability_description': 'Good for mild weather, offering comfort and durability, though they may get damp in high precipitation.'
                }
            ],
            'color_matches_from_outfit': 'The black jacket pairs well with the light blue T-shirt and blue jeans, creating a balanced and coordinated outfit.'
        }
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
                    {}
                    Previous outfit: {}
                    Represent your answer strictly in JSON. Use and fill template: {} 
                    No other comments
                    
                    
                    """,
            },
        ]

    def predict(self, clothes, weather, outfit, hours):
        messages = deepcopy(self.messages)
        messages[-1]["content"] = self.main_content.format(
            clothes, weather, hours, outfit, self.answer_template
        ) + self.example
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
