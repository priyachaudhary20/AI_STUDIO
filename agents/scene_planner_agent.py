import json
import os
from utils.llm import ask_llm


def generate_storyboard(script, characters):

    with open("prompts/scene_prompt.txt", encoding="utf-8") as f:
        base_prompt = f.read()

    prompt = (
        base_prompt
        + "\n\nCHARACTERS:\n"
        + json.dumps(characters)
        + "\n\nSCRIPT:\n"
        + json.dumps(script)
    )

    result = ask_llm(prompt)

    result = result.replace("```json", "").replace("```", "").strip()

    storyboard = json.loads(result)

    os.makedirs("output", exist_ok=True)

    with open("output/storyboard.json", "w", encoding="utf-8") as f:
        json.dump(storyboard, f, indent=2)

    return storyboard