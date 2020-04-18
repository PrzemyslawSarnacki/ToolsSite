import youtube_dl
import os
import zipfile


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
        info = ydl.extract_info(link, download=False)
        filename = os.path.basename(ydl.prepare_filename(info))
    print(filename)
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
        info = ydl.extract_info(link, download=True)
        filename = os.path.basename(ydl.prepare_filename(info))
    return filename

def download_playlist(link):
    dir_name = r"C:/Users/Przemyslaw/Projects/ToolsSite/core/downloads/"
    ydl_opts = {
        "outtmpl": "/core/downloads/%(title)s.%(ext)s",
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(link, download=True)
        filenames = []
        for video in info['entries']:
            if not video:
                print('ERROR: Unable to get info. Continuing...')
                continue
            title = video.get('title').replace(":", " -")
            filenames.append(f"{title}.{video.get('ext')}")
    zip_file = zipfile.ZipFile(f"{dir_name}down.zip", 'w')
    with zip_file:
        for filename in filenames:
            zip_file.write(f"{dir_name}{filename}", arcname=filename)
    return "down.zip"
