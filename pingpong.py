from pygame import *

''' НАСТРОЙКА ОКНА'''
W, H = 600, 500
window = display.set_mode((W, H))
display.set_caption('Пинг Понг')
back = (3, 252, 244)
window.fill(back)
''' ИГРОВОЙ ТАЙМЕР '''
clock = time.Clock()
FPS = 60
''' ИГРОВОЙ ЦИКЛ'''
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)