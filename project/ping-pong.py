from pygame import *


class GamsSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, 
    player_speed, wight, height):
        super().__init__()
        self.image=transform.scale(image.load(player_image),(wight,height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GamsSprite):
    def update_r(self):
        keys = key.get_pressed()
        if key[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed 
    
    def update_l(self):
        keys = key.get_pressed()
        if key[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed 

back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

game = True
finish = True
racket1 = Player('racket.png', 30, 200, 4, 50, 150)
racket2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = GamsSprite('tenis_ball.png', 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

speed_x = 3
speed_y = 3 

clock = time.Clock()
FPS = 60

while game:
    # if finish != True:
    #     window.fill(back)
    display.update()
    clock.tick(FPS)