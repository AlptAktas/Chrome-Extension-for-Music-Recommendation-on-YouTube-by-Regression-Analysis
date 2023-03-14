from pytube.exceptions import PytubeError
from pytube import YouTube
import os


def pytube_downloader(youtube_url):
    try:
        yt = YouTube(youtube_url)
    except PytubeError:
        return False, '0'
    else:
        try:
            video = yt.streams.filter(only_audio=True).first()
        except PytubeError:
            return False, '0'
        except KeyError:
            return False, '0'
        else:
            print('Downloading -----> ' + yt.title)
            out_file = video.download(output_path='data/test_audio/')
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            head, tail = os.path.split(new_file)
            return True, tail


# pytube_downloader("https://www.youtube.com/watch?v=WT7cTpJ_VVY")
