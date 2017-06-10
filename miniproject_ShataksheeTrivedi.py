import pyautogui as pag

x=int(input("enter x-coordinates "))
y=int(input("enter y-coordinates "))
no=int(input("enter number of times you want to make the pattern "))
draw=input("enter the shape you want to draw"
           "triangle/"
           "square/"
           "rectangle/"
           "pentagon/"
           "circle ")
z=0
pag.hotkey('win','r')
pag.typewrite('mspaint')
pag.press('enter')

pag.click(x=176,y=115,clicks=1,button='left', duration=1)

if draw == 'rectangle':
    for a in range (0,no):
        pag.moveTo(x+z,y+z,duration=0.1)
        pag.dragRel(400,0,duration =0.1)
        pag.dragRel(0,200,duration=0.1)
        pag.dragRel(-400,0,duration=0.1)
        pag.dragRel(0,-200,duration=0.1)
        z+=20

elif draw == 'triangle':
    for a in range (0,no):
        pag.moveTo(x + z, y + z, duration=0.1)
        pag.dragRel(200,200,duration=0.1)
        pag.dragRel(-400 ,0,duration=0.1)
        pag.dragTo((x+z),(y+z),duration=0.1)
        z+=20

elif draw == 'square':
    for a in range (0,no):
        pag.moveTo(x+z,y+z,duration=0.1)
        pag.dragRel(200,0,duration =0.1)
        pag.dragRel(0,200,duration=0.1)
        pag.dragRel(-200,0,duration=0.1)
        pag.dragRel(0,-200,duration=0.1)
        z+=20

elif draw == 'pentagon':
    for a in range(0, no):
        pag.moveTo(x + z, y + z, duration=0.1)
        pag.dragRel(150,100, duration=0.1)
        pag.dragRel(0, 200, duration=0.1)
        pag.dragRel(-300, 0, duration=0.1)
        pag.dragRel(0, -200, duration=0.1)
        pag.dragTo((x + z), (y + z), duration=0.1)
        z += 20

elif draw == 'circle':
    for a in range(0, no):
        pag.click(x=384,y=172,clicks=1,button='left', duration=1)
        pag.click(x=229,y=237,clicks=1,button='left', duration=1)
        pag.moveTo(x+z,y+z,duration=0.1)
        pag.dragRel(200,200, duration=0.1)
        z+=20

