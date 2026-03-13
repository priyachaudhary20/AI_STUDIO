import os
import asyncio
import edge_tts

VOICE_MAP = {
    "Mia": "en-US-AriaNeural",
    "Leader": "en-US-GuyNeural",
    "Engineer": "en-GB-RyanNeural",
    "Young Survivor": "en-US-JennyNeural"
}

DEFAULT_VOICE = "en-US-AriaNeural"


async def synthesize(text, voice, filename):
    communicate = edge_tts.Communicate(text=text, voice=voice)
    await communicate.save(filename)


def generate_dialogue_audio(script):

    os.makedirs("assets/audio", exist_ok=True)

    index = 1

    for scene in script["scenes"]:
        for line in scene["dialogue"]:

            character = line["character"]
            text = line["line"]

            voice = VOICE_MAP.get(character, DEFAULT_VOICE)

            filename = f"assets/audio/line_{index}.mp3"

            print("Generating voice:", filename)

            asyncio.run(synthesize(text, voice, filename))

            index += 1