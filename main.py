import pyscreenshot as ImageGrab
import time
import pyscreeze
import os
import time


cmdL = """
osascript -e 'tell application "System Events" to key code 123'
"""
cmdR = """
osascript -e 'tell application "System Events" to key code 124'
"""
cmdSafari = """
osascript -e 'tell application "System Events" to tell process "Safari"
    set frontmost to true
end tell'
"""

branchColor = (160, 115, 61, 255)

def osfunc(cmd):
    os.system(cmd)


def do_things(pxL, pxR):
    if pxL == branchColor:
        print ('left')
        osfunc(cmdR)
        osfunc(cmdR)
        return True
    elif pxR == branchColor:
        print ('right')
        osfunc(cmdL)
        osfunc(cmdL)
        return True
    return False


def main():
    print(time.clock())
    idx = 0
    limit = 500

    osfunc(cmdSafari)

    while idx < limit:
        idx += 1
        im = ImageGrab.grab(bbox=(900, 185, 1050, 415))

        pxL = im.getpixel((60, 415))
        pxR = im.getpixel((220, 415))
        if not do_things(pxL, pxR):
            continue

        pxL = im.getpixel((60, 215))
        pxR = im.getpixel((220, 215))
        if not do_things(pxL, pxR):
            continue

        pxL = im.getpixel((60, 15))
        pxR = im.getpixel((220, 15))
        if not do_things(pxL, pxR):
            continue


main()

