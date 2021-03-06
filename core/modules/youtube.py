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
        info = ydl.extract_info(link, download=True)
        filename = os.path.basename(ydl.prepare_filename(info))
    print(filename)
    return filename


def download_mp3(link):
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "/core/downloads/%(title)s.mp3",
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
    print(filename)    
    return filename

def download_playlist(link, DOWNLOAD_FOLDER):
    ydl_opts = {
        "outtmpl": "/core/downloads/%(title)s.%(ext)s",
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(link, download=True)
        filenames = []
        forbidden_chars = {":": " -", '"': "'"} 
        for video in info['entries']:
            if not video:
                print('ERROR: Unable to get info. Continuing...')
                continue
            title = video.get('title')
            for key in forbidden_chars.keys():
                title.replace(key, forbidden_chars[key])
            filenames.append(f"{title}.{video.get('ext')}")
    zip_file = zipfile.ZipFile(f"{DOWNLOAD_FOLDER}/down.zip", 'w')
    with zip_file:
        for filename in filenames:
            zip_file.write(f"{DOWNLOAD_FOLDER}/{filename}", arcname=filename)
    return "down.zip"

def download_mp3_playlist(link, DOWNLOAD_FOLDER):
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "/core/downloads/%(title)s.mp3",
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
        filenames = []
        for video in info['entries']:
            if not video:
                print('ERROR: Unable to get info. Continuing...')
                continue
            title = video.get('title').replace(":", " -").replace('"',"'")
            filenames.append(f"{title}.mp3")
    zip_file = zipfile.ZipFile(f"{DOWNLOAD_FOLDER}/down.zip", 'w')
    with zip_file:
        for filename in filenames:
            zip_file.write(f"{DOWNLOAD_FOLDER}/{filename}", arcname=filename)
    return "down.zip"

