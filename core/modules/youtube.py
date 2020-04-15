import youtube_dl

def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

def verify(link):
    if "www.youtube.com" in link or "youtu.be" in link:
        return True
    return False


def download_video(link):
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])


def download_mp3(link):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'progress_hooks': [my_hook],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

download_mp3("https://www.youtube.com/watch?v=OYUEZzinoLM")