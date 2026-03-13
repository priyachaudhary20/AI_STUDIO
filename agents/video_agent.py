from moviepy import *
from moviepy.audio.fx.MultiplyVolume import MultiplyVolume
import os


def build_video():

    image_folder = "assets/images"
    audio_folder = "assets/audio"
    music_path = "assets/music/background.mp3"

    # only load image files
    images = sorted([
        img for img in os.listdir(image_folder)
        if img.endswith(".png") or img.endswith(".jpg")
    ])

    # only load mp3 files
    audios = sorted([
        a for a in os.listdir(audio_folder)
        if a.endswith(".mp3")
    ])

    clips = []
    audio_clips = []

    audio_index = 0

    for img in images:

        image_path = os.path.join(image_folder, img)
        clip = ImageClip(image_path)

        # cinematic zoom
        clip = clip.resized(lambda t: 1 + 0.02 * t)

        if audio_index < len(audios):

            audio_path = os.path.join(audio_folder, audios[audio_index])
            speech = AudioFileClip(audio_path)

            duration = speech.duration

            audio_clips.append(speech)

            audio_index += 1

        else:

            duration = 9

        clip = clip.with_duration(duration)

        clips.append(clip)

    # build video sequence
    video = concatenate_videoclips(clips, method="compose")

    # combine speech audio sequentially
    if audio_clips:
        final_speech = concatenate_audioclips(audio_clips)
    else:
        final_speech = None

    # BACKGROUND MUSIC
    if os.path.exists(music_path):

        music = AudioFileClip(music_path)

        # repeat music to cover video duration
        loops = int(video.duration // music.duration) + 1
        music_clips = [music] * loops
        music = concatenate_audioclips(music_clips)

        music = music.with_duration(video.duration)

        # reduce music volume
        music = music.with_effects([MultiplyVolume(0.2)])

        if final_speech:
            final_audio = CompositeAudioClip([music, final_speech])
        else:
            final_audio = music

    else:

        final_audio = final_speech

    # attach audio to video
    if final_audio:
        final_audio = final_audio.with_duration(video.duration)
        video = video.with_audio(final_audio)

    os.makedirs("output", exist_ok=True)

    video.write_videofile(
        "output/final_video.mp4",
        fps=24,
        codec="libx264",
        audio_codec="aac"
    )