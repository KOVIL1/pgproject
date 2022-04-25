from pygame import *

window = display.set_mode((700,500)) 
display.set_caption("Пинг Понг")
background = transform.scale(image.load("blackgrow.jpg"),(700, 500))

game = True
while game:
    window.blit(background, (0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False

window.blit(background, (0, 0))
display.update()