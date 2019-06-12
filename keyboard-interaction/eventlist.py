#!/usr/bin/env python

# This program helps you see how
# to implement very non-interactive status displays, or even
# a crude text output control.

from pygame import *

ImgOnOff = []
Font = None
LastKey = None

def showtext(win, pos, text, color, bgcolor):
    textimg = Font.render(text, 1, color, bgcolor)
    win.blit(textimg, pos)
    return pos[0] + textimg.get_width() + 5, pos[1]


def drawstatus(win):
    bgcolor = 50, 50, 50
    win.fill(bgcolor, (0, 0, 640, 120))
    win.blit(Font.render('Status Area', 1, (155, 155, 155), bgcolor), (2, 2))

    pos = showtext(win, (10, 30), 'Mouse Focus', (255, 255, 255), bgcolor)
    win.blit(ImgOnOff[mouse.get_focused()], pos)

    pos = showtext(win, (10, 60), 'Mouse Position', (255, 255, 255), bgcolor)
    p = '%s, %s' % mouse.get_pos()
    pos = showtext(win, pos, p, bgcolor, (255, 255, 55))

    pos = showtext(win, (330, 60), 'Last Keypress', (255, 255, 255), bgcolor)
    if LastKey:
        p = '%s' % getKeyLetter(LastKey)
    else:
        p = 'None'
    pos = showtext(win, pos, p, bgcolor, (255, 255, 55))

    pos = showtext(win, (10, 90), 'Input Grabbed', (255, 255, 255), bgcolor)
    win.blit(ImgOnOff[event.get_grab()], pos)

def getKeyLetter(keyValue):
    return key.name(keyValue)

def main():
    init()

    win = display.set_mode((640, 480), RESIZABLE)
    display.set_caption("Mouse Focus Workout")

    global Font
    Font = font.Font(None, 26)

    global ImgOnOff
    ImgOnOff.append(Font.render("Off", 1, (0, 0, 0), (255, 50, 50)))
    ImgOnOff.append(Font.render("On", 1, (0, 0, 0), (50, 255, 50)))

    history = []

    going = True
    while going:
        for e in event.get():
            if e.type == QUIT:
                going = False
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    going = False
                else:
                    global LastKey
                    LastKey = e
            if e.type == MOUSEBUTTONDOWN:
                event.set_grab(1)
            elif e.type == MOUSEBUTTONUP:
                event.set_grab(0)
            if e.type == VIDEORESIZE:
                win = display.set_mode(e.size, RESIZABLE)

            if e.type != MOUSEMOTION:
                txt = '%s: %s' % (event.event_name(e.type), e.dict)
                img = Font.render(txt, 1, (50, 200, 50), (0, 0, 0))
                history.append(img)
                history = history[-13:]


        drawstatus(win)

        display.flip()
        time.wait(10)

    quit()



main()
