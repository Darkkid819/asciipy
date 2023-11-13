ASCII Video Player
==================

ASCII Video Player is a Python application that allows you to play videos as ASCII animations in the terminal. It downloads videos, extracts audio, and converts video frames to ASCII art for playback.

Features
--------

* Download videos from YouTube for ASCII playback.
* Extract and play audio from video files.
* Convert video frames to ASCII art.
* Customize frame rate and video resolution through a configuration file.

Requirements
------------

* Python 3
* `yt-dlp`
* `ffmpeg`
* `numpy`
* `PIL` (Pillow)

Installation
------------

1. Clone the repository to your local machine.
2. Ensure `ffmpeg` is installed on your system.
3. Install the required Python packages:

   .. code:: bash

       pip install -r requirements.txt

Usage
-----

To use ASCII Video Player, run the `main.py` script from the command line. You can configure settings using the `config` command or play a video using the `play` command.

Configuration:

.. code:: bash

    python main.py config --set-frame-rate 30 --set-resolution 720p

Playing a video:

.. code:: bash

    # Play a video from a YouTube URL
    python main.py play --url 'https://www.youtube.com/watch?v=example'

    # Play a video from a local file
    python main.py play --file '/path/to/your/video.mp4'

The application will clean up previous downloads and frames before processing a new video. During processing, a spinning cursor will display as a progress indicator.

Contributing
------------

Contributions are welcome! Please feel free to submit pull requests or create issues for bugs and feature requests.

License
-------

ASCII Video Player is released under the MIT License. See the LICENSE file for more details.
