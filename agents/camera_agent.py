import json
from utils.llm import ask_llm


def generate_camera_plan(script):

    prompt = open("prompts/camera_prompt.txt").read()

    result = ask_llm(prompt + json.dumps(script))

    return json.loads(result)