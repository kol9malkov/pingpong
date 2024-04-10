from pygame import *
from pygame.sprite import _Group

''' КЛАССЫ '''
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


''' НАСТРОЙКА ОКНА'''
W = 600
H = 500
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