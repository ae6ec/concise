from __future__ import unicode_literals
from dataclasses import dataclass
import youtube_dl
import webvtt
import requests
from io import StringIO
import re

# Includes vtt to text conversion
# TODO: add seperate module
# TODO: add more lagnuages
# TODO: add subtilte


class Error(Exception):
    """Base class for other exceptions"""

    pass


class NoEnglishSubtitleFound(Error):
    """Raised when the no english subtitle found"""

    pass


class NoSubtitleFound(Error):
    """Raised when the No subtitle found"""

    pass


class MyLogger(object):
    def debug(self, msg):
        print("Debug:" + msg)

    def warning(self, msg):
        print("Warning:" + msg)

    def error(self, msg):
        print("Error:" + msg)


ydl_opts = {
    # "writesubtitles": True,
    # "subtitleslangs": ["en", "en-GB", "en-CA"],
    # "writeautomaticsub": True,
    # "verbose": True,
    # "subtitlesformat": "vtt",
    "skip_download": True,
    # "postprocessors": [
    #     {
    #         "key": "FFmpegSubtitlesConvertor",
    #         "format": "vtt",
    #     },
    # ],
    "logger": MyLogger(),
    "noplaylist": True,
    "outtmpl": "%(id)s.%(ext)s",
}

# TODO: add second loop to a function and better error handling


def getVidDataSub(data, key):
    flag = False

    if key not in data:
        return False, None

    for i in data[key]:
        check = re.match("^(en)+", i)
        if check:
            flag = True
            for j in data[key][i]:
                if j["ext"] == "vtt":
                    return True, j
    return flag, None


def youtube_sub(url):
    error = None
    sub = ""
    subdata = {}
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            vidData = ydl.extract_info(url, download=False)

            subdata = getVidDataSub(vidData, "subtitles")
            capdata = getVidDataSub(vidData, "automatic_captions")

            if capdata[1] == None and subdata[1] == None:
                raise NoSubtitleFound
            if capdata[0] == False and subdata[1] == False:
                raise NoEnglishSubtitleFound
            subdata = subdata[1] if subdata[1] != None else capdata[1]

        payload = requests.get(subdata["url"]).text
        buffer = StringIO(payload)

        for caption in webvtt.read_buffer(buffer):
            sub += caption.text

    except NoSubtitleFound:
        error = "No subtitle Present"

    except NoEnglishSubtitleFound:
        error = "No english subtitle Present "

    except Exception as e:
        print("Error:", e)
        error = e
    return sub, error


def test_youtube_sub():
    # print("NO sub", youtube_sub("https://www.youtube.com/watch?v=cfPv86XMsXI"))
    # print(
    #     "Aurtomatic Caption ",
    #     youtube_sub("https://www.youtube.com/watch?v=FSU5_TqQuA8"),
    # )
    print("Test", youtube_sub("https://www.youtube.com/watch?v=R9OCA6UFE-0"))


if __name__ == "__main__":
    test_youtube_sub()
