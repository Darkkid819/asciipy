import os
import json
import time
import curses
import subprocess
import threading
from collections import deque

from ascii_conversion import image_to_ascii

BUFFER_SIZE = 180  # Adjust based on system's memory & frame sizes


def play_audio(audio_path):
    command = ["ffplay", "-nodisp", "-autoexit", audio_path]
    subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)


def load_config():
    config_file = os.path.join('assets', 'config.json')
    with open(config_file, 'r') as f:
        return json.load(f)


def play_animation(video_path, charset=None):
    config = load_config()
    frame_rate = config["frame_rate"]

    audio_output_filename = os.path.join('assets', 'downloads', f"{os.path.basename(video_path).split('.')[0]}.mp3")
    frame_folder = os.path.join('assets', 'frames')

    frame_files = [f for f in os.listdir(frame_folder) if f.endswith('.jpg')]
    frame_files.sort(key=lambda x: int(x.split('_')[1].split('.')[0]))

    audio_thread = threading.Thread(target=play_audio, args=(audio_output_filename,))
    audio_thread.start()

    start_time = time.time()
    curses.wrapper(lambda stdscr: draw_frames(stdscr, frame_files, charset, frame_rate, start_time))


def draw_frames(stdscr, frame_files, charset, frame_rate, start_time):
    buffer = deque()
    frame_duration = 1.0 / frame_rate
    frame_index = 0
    max_height, max_width = stdscr.getmaxyx()

    try:
        while frame_files or buffer:
            while frame_files and len(buffer) < BUFFER_SIZE:
                frame_file = frame_files.pop(0)
                frame_path = os.path.join('assets', 'frames', frame_file)
                buffer.append(image_to_ascii(frame_path, max_width-1, max_height, charset))

            if buffer:
                ascii_frame = buffer.popleft()

                stdscr.erase()
                stdscr.addstr(0, 0, ascii_frame)
                stdscr.refresh()

                current_time = time.time()
                sleep_duration = max((frame_index + 1) * frame_duration - (current_time - start_time), 0)
                time.sleep(sleep_duration)

                frame_index += 1

    except KeyboardInterrupt:
        print("Interrupted by user, shutting down.")
