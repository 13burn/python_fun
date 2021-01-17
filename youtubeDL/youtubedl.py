import eel
import os
import pytube

CURRENT_DIR = os.getcwd()

eel.init("front")

@eel.expose
def downloader(link):
    try:
        os.chdir(f"{os.environ['USERPROFILE']}/Videos")
        eel.statusPrint("Downloading...")
        pytube.YouTube(link).streams.first().download()
        os.chdir(CURRENT_DIR)
        eel.statusPrint("Downloaded...")

    except:
        os.chdir(CURRENT_DIR)
        eel.statusPrint("Unable to download, please verify the link.")


eel.start("front.html")