import youtube_dl
import os


def my_hook(d):
    if d["status"] == "finished":
        print("Done downloading, now converting ...")


def verify(link):
    if "www.youtube.com" in link or "youtu.be" in link:
        return True
    return False


def download_video(link):
    ydl_opts = {
        "outtmpl": "/core/downloads/%(title)s.%(ext)s",
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(link, download=True)
        filename = os.path.basename(ydl.prepare_filename(info))
    return filename


def download_mp3(link):
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "/core/downloads/%(title)s.%(ext)s",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],  
        "progress_hooks": [my_hook],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print(ydl_opts["outtmpl"])
        result = ydl.download([link])
        print(ydl_opts["outtmpl"])
        filename = ydl.prepare_filename(result)
        print(ydl_opts["outtmpl"])
        print(filename)

    return filename

def download_playlist(parameter_list):
    pass
