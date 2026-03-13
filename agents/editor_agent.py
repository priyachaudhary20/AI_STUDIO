from moviepy import *


def finalize():

    video = VideoFileClip("output/final_video.mp4")

    music = AudioFileClip("assets/music/background.mp3").volumex(0.2)

    final = video.set_audio(music)

    final.write_videofile("output/final_video.mp4")