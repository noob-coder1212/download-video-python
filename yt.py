import argparse
from pytube import YouTube

parser = argparse.ArgumentParser()
parser.add_argument('-y', '--youtube', type=str, help='download youtube')
args = parser.parse_args()

if args.youtube:
    SAVE_PATH = "E:/"
    yt = YouTube(args.youtube)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(SAVE_PATH)
