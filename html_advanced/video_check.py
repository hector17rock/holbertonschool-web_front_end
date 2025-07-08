#!/usr/bin/env python3
import re


def check_video_source():
    try:
        with open('38-styleguide.html', 'r') as f:
            content = f.read()

        # Check if the video has the correct source URL
        video_url = (
            'https://intranet-projects-files.s3.amazonaws.com/webstack/'
            'BigBuckBunny.mp4'
        )
        if video_url in content:
            print("video has correct source")
        else:
            print("video source not found or incorrect")

    except FileNotFoundError:
        print("38-styleguide.html not found")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    check_video_source()
