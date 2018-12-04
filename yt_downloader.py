import pytube as pt
import pydub
from pydub import AudioSegment
import os
from sys import stdout

url = 'https://www.youtube.com/watch?v=f4Mc-NYPHaQ'

def download_mp4(url, cb=None):
    yt = pt.YouTube(url)
    if cb:
        yt.register_on_progress_callback(cb)
    stream = yt.streams.filter(progressive=True).order_by('resolution').desc().first()
    stream.download()

def download_mp3(url, cb=None, cb_after_download=None, cb_convert=None):
    yt = pt.YouTube(url)
    if cb:
        yt.register_on_progress_callback(cb)
    stream = yt.streams.filter(progressive=True, subtype='mp4', resolution='360p').first()
    stream.download(filename='tmp')
    if cb_after_download:
        cb_after_download()

    chunk_size = 5000
    sound = AudioSegment.from_file('tmp.mp4')
    duration = sound.duration_seconds * 1000 / chunk_size
    try:
        os.remove(yt.title + '.mp3')
    except OSError:
        pass
    with open(yt.title + '.mp3', 'ab') as f:
        for i, chunk in enumerate(sound[::chunk_size]):
            chunk.export(f, format="mp3")
            if(cb_convert):
                cb_convert(i, duration)
    # AudioSegment.from_file('tmp.mp4').export(yt.title + '.mp3', format='mp3')
    os.remove('tmp.mp4')
