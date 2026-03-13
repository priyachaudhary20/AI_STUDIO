from agents.story_agent import generate_story
from agents.character_agent import generate_characters
from agents.scene_planner_agent import generate_storyboard
from agents.image_agent import generate_images
from agents.voice_agent import generate_dialogue_audio
from agents.video_agent import build_video


def run_pipeline():

    print("Generating characters...")
    characters = generate_characters()

    print("Generating story...")
    story = generate_story()

    print("Planning scenes...")
    storyboard = generate_storyboard(story, characters)

    print("Generating images...")
    generate_images(storyboard,characters)

    print("Generating voice...")
    generate_dialogue_audio(story)

    print("Building video...")
    build_video()

    print("Finished!")


if __name__ == "__main__":
    run_pipeline()