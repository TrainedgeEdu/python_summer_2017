import pyautogui as pag
import math
import time

def openpaint():
    pag.hotkey('win', 'r')
    pag.typewrite('mspaint')
    pag.press('enter')
def choose():
    print('press 1 for predefined values')
    print('press 2 for defined values')
    b=int(input())
    return b
def makecircle(r,times) :

 x,y,c=500,500,1
 openpaint()
 while c<=times:
   cx,cy=x,y
   radius=r
   angle=0
   omega=0.3

   pag.moveTo(x, y, duration=1)
   x=cx+radius*math.cos(angle)
   y = cy + radius * math.sin(angle)
   pag.click(x,y)
   while 2*math.pi-angle>=0.001:
       angle+=omega
       x+=radius*omega*math.cos(angle+math.pi/2)
       y += radius * omega * math.sin(angle + math.pi / 2)
       pag.dragTo(x,y,duration=0.2)
   x+=10
   y+=10
   c+=1
def makerect(length,breadth,times):
    x, y, k = 730, 438, 0
    openpaint()
    while k<times :
         pag.moveTo(x, y, duration=1)
         pag.dragTo(x + length, y, duration=0.1)
         pag.dragTo(x + length, y - breadth, duration=0.1)
         pag.dragTo(x, y - breadth, duration=0.1)
         pag.dragTo(x, y, duration=0.1)
         k+=1
         x+=10
         y+=10

def maketriangle(x1,y1,x2,y2,x3,y3,times) :
    openpaint()
    k=0
    while k< times:
     pag.moveTo(x1, y1, duration=1)
     pag.dragTo(x2, y2, duration=0.1)
     pag.dragTo(x3, y3, duration=0.1)
     pag.dragTo(x1, y1, duration=0.1)
     k+=1
     x1+=10
     y1+=10
     x2+=10
     y2+=10
     x3+=10
     y3+=10

print('choose')
print('press 1 to draw a circle')
print('press 2 to draw a square')
print('press 3 to draw a rectangle')
print('press 4 to draw a triangle')
a = int(input())
if a == 1:
    times=int(input('no.of times'))
    b=choose()
    if b==1:
         makecircle(100,times)
    if b==2:
         radius=int(input('enter length'))
         makecircle(radius,times)


if a == 2:
    times=int(input('no.of times'))
    b=choose()
    if b==1:
         makerect(100,100,times)
    if b==2:
         length=int(input('enter length'))
         makerect(length,length,times)
if a == 3:
    times=int(input('the number of times'))
    b=choose()
    if b==1:
       makerect(300,250,times)
    if b==2:
        length=int(input('enter length'))
        breadth = int(input('enter length'))
        makerect(length,breadth,times)
if a == 4 :
    times = int(input('the number of times'))
    b=choose()
    if b==1 :
        maketriangle(730,436,450,300,830,500,times)
    if  b == 2 :
      x1,y1=int(input('first coordinate'))
      x2, y2 = int(input('second coordinate'))
      x3, y3 = int(input('third coordinate'))
      maketriangle(x1, y1, x2, y2, x3, y3,times)
      # myprogramms/pyautogui 