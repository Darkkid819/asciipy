import os
import shutil


def cleanup():
    assets_folder = os.path.join('assets')
    downloads_folder = os.path.join(assets_folder, 'downloads')
    frames_folder = os.path.join(assets_folder, 'frames')

    os.makedirs(assets_folder, exist_ok=True)

    if os.path.exists(downloads_folder):
        shutil.rmtree(downloads_folder)
    os.makedirs(downloads_folder)

    if os.path.exists(frames_folder):
        shutil.rmtree(frames_folder)
    os.makedirs(frames_folder)
