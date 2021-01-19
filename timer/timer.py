import eel

eel.init("front")

@eel.expose
def converter(minutes, seconds):
    minute = int(minutes) * 60
    second = minute + int(seconds)
    eel.countDown(second)
    print("python ok")
    
eel.start("front.html")