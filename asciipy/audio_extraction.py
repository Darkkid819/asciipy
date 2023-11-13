import os
import subprocess


def extract_audio(video_path):
    output_folder = os.path.join('assets', 'downloads')
    audio_output_filename = os.path.join(
        output_folder,
        f"{os.path.basename(video_path).split('.')[0]}.mp3"
    )

    command = [
        "ffmpeg", "-i", video_path,
        "-q:a", "0", "-map", "a",
        audio_output_filename
    ]

    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    return audio_output_filename
