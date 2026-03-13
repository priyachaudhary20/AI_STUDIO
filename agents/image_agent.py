import os
import requests
from dotenv import load_dotenv

load_dotenv()

STABILITY_KEY = os.getenv("STABILITY_API_KEY")


def generate_image(prompt, filename):

    url = "https://api.stability.ai/v2beta/stable-image/generate/core"

    headers = {
        "Authorization": f"Bearer {STABILITY_KEY}",
        "Accept": "image/*"
    }

    files = {
        "prompt": (None, prompt),
        "output_format": (None, "png")
    }

    response = requests.post(url, headers=headers, files=files)

    if response.status_code != 200:
        print("Image generation failed:")
        print(response.text)
        return False

    with open(filename, "wb") as f:
        f.write(response.content)

    return True


def generate_images(storyboard, characters):

    os.makedirs("assets/images", exist_ok=True)

    mia_prompt = ""

    if isinstance(characters, dict) and "characters" in characters:
        character_list = characters["characters"]
    elif isinstance(characters, list):
        character_list = characters
    else:
        raise ValueError("Invalid characters format returned from character agent")

    for c in character_list:
        if c["name"].lower() == "mia":
            mia_prompt = c["image_prompt"]

    for scene in storyboard["scenes"]:
        for shot in scene["shots"]:

            prompt = f"""
            cinematic film still,
            post-apocalyptic sci-fi world,
            dramatic cinematic lighting,
            35mm film look,
            high detail,
            {shot['visual_prompt']}

            Main character Mia:
            {mia_prompt}

            consistent character design
            """

            filename = f"assets/images/scene{scene['scene_number']}_shot{shot['shot']}.png"

            print("Generating:", filename)

            success = generate_image(prompt, filename)

            if not success:
                print("Skipping image due to error.")