import json
import re
import os
from utils.llm import ask_llm


def generate_story():

    with open("prompts/story_prompt.txt", encoding="utf-8") as f:
        prompt = f.read()

    response = ask_llm(prompt)

    response = response.replace("```json", "").replace("```", "").strip()

    match = re.search(r"\{.*\}", response, re.DOTALL)

    if not match:
        raise ValueError("No JSON found in LLM response")

    json_text = match.group(0)

    try:
        story = json.loads(json_text)

    except json.JSONDecodeError as e:
        print("Invalid JSON from model")
        print(json_text)
        raise

    os.makedirs("output", exist_ok=True)

    with open("output/script.json", "w", encoding="utf-8") as f:
        json.dump(story, f, indent=2)

    return story