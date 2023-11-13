import json
import os
import subprocess


def extract_frames(video_path):
    config_file = os.path.join('assets', 'config.json')

    with open(config_file, 'r') as config_file:
        config = json.load(config_file)

    frame_rate = config.get("frame_rate", 24)  # 24 is default if not found

    output_folder = os.path.join('assets', 'frames')

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    command = [
        "ffmpeg", "-i", video_path,
        "-vf", f"fps={frame_rate}",
        "-r", str(frame_rate),
        os.path.join(output_folder, "frame_%d.jpg")
    ]

    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
