#!/usr/bin/env python
# coding=utf-8

import pyautogui as pag
import time


def openShell():
    pag.keyDown('winleft')
    pag.press('enter')
    pag.keyUp('winleft')
    time.sleep(1)


def setVertical():
    pag.keyDown('winleft')
    pag.press('v')
    pag.keyUp('winleft')


def setHorizontal():
    pag.keyDown('winleft')
    pag.press('g')
    pag.keyUp('winleft')


def openEmacs():
    pag.keyDown('winleft')
    pag.press('z')
    pag.keyUp('winleft')


def openRanger():
    pag.keyDown('winleft')
    pag.press('c')
    pag.keyUp('winleft')


def openQutebrowser():
    pag.keyDown('winleft')
    pag.press('t')
    pag.keyUp('winleft')


def openSyncthing():
    openShell()
    pag.typewrite('syncthing -no-browser')
    pag.press('enter')


def openMakesexy():
    openShell()
    pag.typewrite('python3 makesexy.py')
    pag.press('enter')


def openTransmission():
    setHorizontal()
    openShell()
    pag.keyDown('winleft')
    pag.keyDown('shift')
    pag.press('l')
    pag.keyUp('shift')
    pag.keyUp('winleft')

    pag.typewrite('transmission-daemon')
    pag.press('enter')
    time.sleep(1)
    pag.typewrite('transmission-remote-cli')
    pag.press('enter')
    time.sleep(1)


def resize(n, dir):
    pag.keyDown('winleft')
    pag.press('r')
    pag.keyUp('winleft')
    for i in range(n):
        pag.press(dir)
    pag.press('escape')


def gotoWorkspace(workspaceId):
    pag.keyDown('winleft')
    pag.press(str(workspaceId))
    pag.keyUp('winleft')


def sendtoWorkspace(workspaceId):
    pag.keyDown('winleft')
    pag.keyDown('shift')
    pag.press(str(workspaceId))
    pag.keyUp('shift')
    pag.keyUp('winleft')


def close():
    pag.keyDown('winleft')
    pag.press('q')
    pag.keyUp('winleft')


def hidemouse():
    pag.keyDown('winleft')
    pag.press('escape')
    pag.keyUp('winleft')


def openGlances():
    openShell()
    time.sleep(5)
    pag.typewrite('glances')
    pag.press('enter')


def focus(dir):
    pag.keyDown('winleft')
    pag.press(dir)
    pag.keyUp('winleft')


hidemouse()
gotoWorkspace(1)
openGlances()
setVertical()
openShell()
resize(1, 'j')
setHorizontal()
openShell()
focus('h')
setVertical()
openShell()

gotoWorkspace(4)
setVertical()
openShell()
openMakesexy()
openTransmission()
resize(3, 'l')
setVertical()
openSyncthing()
resize(3, 'k')
focus('k')

gotoWorkspace(2)
openShell()

gotoWorkspace(3)
openEmacs()
time.sleep(20)
pag.press(',')
pag.press('q')

gotoWorkspace(5)
openRanger()

gotoWorkspace(2)
close()
openQutebrowser()