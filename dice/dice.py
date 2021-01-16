import eel
import random
from time import sleep

eel.init("front")

@eel.expose
def randGen(top):
    for num in range(top):
        #print in front end
        eel.diceShow(random.randint(1,top))
        if top > 100:
            sleep(.015)
        else:
            sleep(.15)
        
eel.start("front.html")

