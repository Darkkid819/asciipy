import os
import json
import yt_dlp as ydlp
from audio_extraction import extract_audio


def download_video(url):
    video_output_template = os.path.join('assets', 'downloads', '%(title)s.%(ext)s')
    config_file = os.path.join('assets', 'config.json')

    with open(config_file, 'r') as config_file:
        config = json.load(config_file)

    resolution = config.get("resolution", "best")  # best is default if not found

    video_filename = None

    def hook(d):
        nonlocal video_filename
        if d['status'] == 'finished':
            video_filename = os.path.abspath(d['filename'])

    ydl_opts = {
        'format': f'bestvideo[height={resolution[:-1]}]+bestaudio/best',
        'outtmpl': video_output_template,
        'progress_hooks': [hook],
        'quiet': True,
        'no_warnings': True
    }

    directory = os.path.dirname(video_output_template)

    if not os.path.exists(directory):
        os.makedirs(directory)

    with ydlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    extract_audio(video_filename)

    return video_filename
