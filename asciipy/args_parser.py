import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="ASCII Video Player")
    subparsers = parser.add_subparsers(dest='command', required=True)

    play_parser = subparsers.add_parser('play', help='Play video as ASCII animation in terminal.')

    group = play_parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--url', type=str, help='YouTube URL to download and play.')
    group.add_argument('--file', type=str, help='Path to local video file to play.')

    config_parser = subparsers.add_parser('config', help='Configure ASCII Video Player settings.')

    config_parser.add_argument('--set-frame-rate', type=int, help='Set the frame rate.')
    config_parser.add_argument('--set-resolution', type=str, help='Set the video resolution.')
    # ... Add other configuration arguments ...

    return parser.parse_args()
