import eel

eel.init("front")

#TODO: change this whole function to JS
@eel.expose
def converter(minutes, seconds):
    minute = int(minutes) * 60
    second = minute + int(seconds)#i'm pretty sure js is sending ints but i haven'ttest it yet
    eel.countDown(second)
    
eel.start("front.html")