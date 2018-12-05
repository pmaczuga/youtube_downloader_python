import pytube as pt
import pydub
from pydub import AudioSegment
import os
from sys import stdout

url = 'https://www.youtube.com/watch?v=f4Mc-NYPHaQ'

def download(url, name=None, quality='good', on_progress=None, on_complete=None, on_error=None):
    try:
        yt = pt.YouTube(url)
        if on_progress:
            def cb(stream, chunk, file_handle, bytes_remaining):
                on_progress(stream.filesize - bytes_remaining, stream.filesize)
            yt.register_on_progress_callback(cb)

        streams = yt.streams.filter(progressive=True, subtype='mp4')
        if quality == 'godd':
            streams = streams.order_by('resolution').desc()
        if quality == 'poor':
            streams = streams.filter(resolution='360p')

        filename = streams.first().download(filename=name)

        if on_complete:
            on_complete()

        return filename

    except Exception as e:
        if on_error:
            on_error(e)

def convert(in_file, out_file, format='mp3', chunk_duration=5000, on_progress=None, on_complete=None, on_error=None):
    try:
        sound = AudioSegment.from_file(in_file)
        chunk_num = sound.duration_seconds * 1000 / chunk_duration
        try:
            os.remove(yt.title + '.mp3')
        except OSError:
            pass
        with open(in_file, 'ab') as f:
            for i, chunk in enumerate(sound[::chunk_duration]):
                chunk.export(f, format=format)
                if(on_progress):
                    on_progress(i, chunk_num)

        if on_complete:
            on_complete()
    except Exception as e:
        if on_error:
            on_error(e)

def download_mp4(url, on_progress=None, on_complete=None, on_error=None):

    download(
        url, 
        quality='good',
        on_progress=on_progress,
        on_complete=on_complete,
        on_error=on_error)

def download_mp3(url, on_progress=None, on_half=None, on_complete=None, on_error=None):
    download(
        url,
        name='tmp',
        quality='poor',
        on_progress=on_progress,
        on_complete=on_complete,
        on_error=on_error)

    on_half()

    convert(
        'tmp.mp3',
        )
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
