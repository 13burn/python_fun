import eel

LOWER_NUMBER = 0
HIGHER_NUMBER = 100
GUESS_NUMBER = 0
TRY_COUNTER = 0



eel.init("front")

@eel.expose
def setNums(lower, higher, count):
    global LOWER_NUMBER
    global HIGHER_NUMBER
    global GUESS_NUMBER
    global TRY_COUNTER
    LOWER_NUMBER = lower
    HIGHER_NUMBER = higher
    GUESS_NUMBER = ((HIGHER_NUMBER - LOWER_NUMBER) // 2) + LOWER_NUMBER
    #print(f"lower:{LOWER_NUMBER}, higher:{HIGHER_NUMBER}, counter:{TRY_COUNTER}, guess:{GUESS_NUMBER}")
    TRY_COUNTER = count
    numberGuess(GUESS_NUMBER)

def numberGuess(guess):
    eel.guessPrint(guess)#this one will create the inner html

@eel.expose
def isLower():
    global LOWER_NUMBER
    global HIGHER_NUMBER
    global TRY_COUNTER
    TRY_COUNTER += 1
    diff = (HIGHER_NUMBER - LOWER_NUMBER) // 2
    setNums(LOWER_NUMBER, LOWER_NUMBER+diff, TRY_COUNTER)

@eel.expose
def isHigher():
    global LOWER_NUMBER
    global HIGHER_NUMBER
    global TRY_COUNTER
    TRY_COUNTER += 1
    diff = (HIGHER_NUMBER - LOWER_NUMBER) // 2
    setNums(LOWER_NUMBER+diff, HIGHER_NUMBER, TRY_COUNTER)

@eel.expose
def correctNumber():
    global TRY_COUNTER
    eel.correctNum(TRY_COUNTER)





eel.start("front.html")