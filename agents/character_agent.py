import json
from utils.llm import ask_llm


def generate_characters():

    with open("prompts/character_prompt.txt", encoding="utf-8") as f:
        prompt = f.read()

    response = ask_llm(prompt)

    response = response.replace("```json", "").replace("```", "").strip()

    characters = json.loads(response)

    with open("output/characters.json", "w", encoding="utf-8") as f:
        json.dump(characters, f, indent=2)

    return characters