import eel
import os
import pytube

os.chdir(f"{os.environ['USERPROFILE']}/Videos")

eel.init("front")

def downloader(link):
    try:
        pytube.YouTube(link).streams.first().download()
    except:
        "Send:unable to download"
        pass


eel.start("front.html")