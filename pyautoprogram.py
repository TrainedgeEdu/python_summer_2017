import pyautogui as pag
import math

pag.FAILSAFE = False

def openPinta():
      pag.hotkey('ctrl','alt','t',pause=1,_pause=True)
      pag.typewrite('pinta')
      pag.press('enter',pause=10,_pause=True)

def choose():
    print("enter 1 for predefined shape")
    print("enter 2 for user defined shape")
    c = int(input())
    return c

def makeCircle(x,y):
    openPinta()
    c = 1
    while c <= times:
        cx, cy = x, y
        radius = 100
        angle = 0
        omega = 0.3

        pag.moveTo(x, y, duration=1)
        # parametric equation of circle
        x = cx + radius * math.cos(angle)
        y = cy + radius * math.sin(angle)
        pag.click(x, y)

        while 2 * math.pi - angle >= 0.001:
            angle += omega
            x += radius * omega * math.cos(angle + math.pi / 2)
            y += radius * omega * math.sin(angle + math.pi / 2)
            pag.dragTo(x, y, duration=0.2)

        x += 10
        y += 10
        c += 1


def makeSquare():
    z = 0
    b=choose()
    if b==1:
        openPinta()
        for i in range(0,times):
            pag.moveTo(457+z, 247+z, duration=.1)
            pag.click(x=457+z, y=247+z, clicks=1, interval=2, button='right')
            pag.dragRel(200, 0, duration=.1)
            pag.dragRel(0, 200, duration=.1)
            pag.dragRel(-200, 0, duration=.1)
            pag.dragRel(0, -200, duration=.1)
            z+=20

    if b==2:
        print("enter x and y co-ordinates between: (211,102) (1012,700")
        x = int(input("enter x co-ordinate:"))
        y = int(input("enter y co-ordinate:"))
        l = int(input("enter the length:"))
        openPinta()
        for a in range(0, times):
            pag.moveTo(x + z, y + z, duration=0.1)
            pag.click(x=x + z, y=y + z, clicks=1, interval=2, button='right')
            pag.dragRel(l, 0, duration=0.1)
            pag.dragRel(0, l, duration=0.1)
            pag.dragRel(-l, 0, duration=0.1)
            pag.dragRel(0, -l, duration=0.1)
            z += 20


def makeRectangle(len, bre):
    z = 0
    b = choose()
    if b == 1:

        openPinta()
        for a in range(0, times):
          pag.moveTo(457+z, 247+z, duration=.1)
          pag.click(x=457+z, y=247+z, clicks=1, interval=2, button='right')
          pag.dragRel(400, 0, duration=.1)
          pag.dragRel(0, 200, duration=.1)
          pag.dragRel(-400, 0, duration=.1)
          pag.dragRel(0, -200, duration=.1)
          z+=20

    if b == 2:

        openPinta()
        for a in range(0, times):
          pag.moveTo(x+z, y+z, duration=.1)
          pag.click(x=x+z, y=x+z, clicks=1, interval=2, button='right')
          pag.dragRel( len, 0, duration=.1)
          pag.dragRel(0,  bre, duration=.1)
          pag.dragRel(-len, 0, duration=.1)
          pag.dragRel(0, -bre, duration=.1)
          z+=20

def makeTriangle():
    z = 0
    b = choose()
    if b == 1:
        openPinta()
        for a in range(0, times):
          pag.moveTo(457+z, 247+z, duration=.1)
          pag.click(x=457+z, y=247+z, clicks=1, interval=2, button='right')
          pag.dragRel(200, 200, duration=.1)
          pag.dragRel(-400, 0, duration=.1)
          pag.dragTo(457+z, 247+z, duration=.1)
          z+=20

    if b == 2:
        print("enter x and y co-ordinates between: (211,102) (1012,700")
        x = int(input("enter x co-ordinate:"))
        y = int(input("enter y co-ordinate:"))
        openPinta()
        for a in range(0, times):
          pag.moveTo(x+z, y+z, duration=.1)
          pag.click(x=x+z, y=y+z, clicks=1, interval=2, button='right')
          pag.dragRel(200, 200, duration=.1)
          pag.dragRel(-400, 0, duration=.1)
          pag.dragTo(x+z, y+z, duration=.1)
          z+=20


print("choose the shape:")
print("press 1 for circle")
print("press 2 for square ")
print("press 3 for triangle")
print("press 4 for rectangle")
print("press 5 for exit")
a=int(input("Your choice: "))
if a==1:
    times = int(input("enter no of times you want to run the loop:"))
    b = choose()
    if b == 1:
        makeCircle(450, 350)
    if b == 2:
        print("enter x and y co-ordinates between: (211,102) (1012,700")
        x = int(input("enter x co-ordinate:"))
        y = int(input("enter y co-ordinate:"))
        makeCircle(x, y)

if a==2:
    times = int(input("enter no of times you want to run the loop:"))
    makeSquare()

if a==3:
    times = int(input("enter no of times you want to run the loop:"))
    makeTriangle()

if a==4:
    times = int(input("enter no of times you want to run the loop:"))
    makeRectangle()

if a==5:
    exit()
