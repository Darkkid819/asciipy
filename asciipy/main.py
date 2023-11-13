from args_parser import parse_args
from animation_playback import play_animation
from progress import start_spinner, stop_spinner
from audio_extraction import extract_audio
from yt_dlp_wrapper import download_video
from frame_extraction import extract_frames
from config_manager import load_config, save_config, set_default_config
from cleanup import cleanup


def main():
    cleanup()

    args = parse_args()
    config = load_config()

    if any(key not in config for key in ["frame_rate", "resolution", "audio", "enhancements"]):
        set_default_config()
        config = load_config()

    if args.command == "config":
        if args.set_frame_rate:
            config["frame_rate"] = args.set_frame_rate
        if args.set_resolution:
            config["resolution"] = args.set_resolution
        # ... Handle other configuration arguments ...

        save_config(config)

    elif args.command == "play":
        spinner_thread = start_spinner()

        if args.url:
            video_path = download_video(args.url)
        else:
            video_path = args.file
            extract_audio(video_path)

        extract_frames(video_path)

        stop_spinner(spinner_thread)

        play_animation(video_path, None)


if __name__ == "__main__":
    main()
