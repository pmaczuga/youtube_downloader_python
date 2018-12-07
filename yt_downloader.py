import pytube as pt
import pydub
from pydub import AudioSegment
import os
from sys import stdout

url = 'https://www.youtube.com/watch?v=f4Mc-NYPHaQ'

def download(url, name=None, quality='good', on_start=None, on_progress=None, on_complete=None, on_error=None):
    try:
        yt = pt.YouTube(url)

        if on_start:
            on_start(yt.title)

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
            on_complete(filename)

        return filename

    except Exception as e:
        print(e)
        if on_error:
            on_error(e)

def convert(in_file, out_file, format='mp3', chunk_duration=5000, on_start=None, on_progress=None, on_complete=None, on_error=None):
    try:
        if on_start:
            on_start()

        sound = AudioSegment.from_file(in_file)
        chunk_num = sound.duration_seconds * 1000 / chunk_duration
        try:
            os.remove(out_file)
        except OSError:
            pass

        with open(out_file, 'ab') as f:
            for i, chunk in enumerate(sound[::chunk_duration]):
                chunk.export(f, format=format)
                if(on_progress):
                    on_progress(i, chunk_num)

        if on_complete:
            on_complete(out_file)

        return out_file

    except Exception as e:
        print(e)
        if on_error:
            on_error(e)

def download_mp4(url, on_start=None, on_progress=None, on_complete=None, on_error=None):

    try:
        download(
            url, 
            quality='good',
            on_start=on_start,
            on_progress=on_progress,
            on_complete=on_complete)

    except Exception as e:
        print(e)
        if on_error:
            on_error(e)

def download_mp3(url, on_start=None, on_progress=None, on_half=None, on_complete=None, on_error=None):
    
    try:
        download(
            url,
            name='tmp',
            quality='poor',
            on_start=on_start,
            on_progress=on_progress)

        on_half()

        convert(
            'tmp.mp4',
            pt.YouTube(url).title + '.mp3',
            format='mp3',
            on_progress=on_progress,
            on_complete=on_complete)

        # os.remove('tmp.mp4')

    except Exception as e:
        print(e)
        if on_error:
            on_error(e)

def get_title(url):
    return pt.YouTube(url).title