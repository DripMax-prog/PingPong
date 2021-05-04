from pygame import *

font.init()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_speed, player_x, player_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (75, 75))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, player_speed, player_x, player_y):
        super().__init__(player_image, player_speed, player_x, player_y)
        self.image = transform.scale(image.load(player_image), (100, 150))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def updateL(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > -70:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed
    def updateR(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > -70:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 400:
            self.rect.y += self.speed

back = (40, 104, 168)

window = display.set_mode((700, 500))
display.set_caption('Ping Pong')
window.fill(back)

kot = GameSprite('POPCAT.png', 3, 350, 250)
right_fighter = Player('DRIPRIGHT.png', 4, 600, 150)
left_fighter = Player('DRIPLEFT.png', 4, 0, 150)

clock = time.Clock()
FPS = 60

lose = font.SysFont('Kohinoor Devanagari', 70)

leftlose = lose.render(
    "Left Player LOSE !", True, (247, 255, 0)
)

rightlose = lose.render(
    "Right Player LOSE !", True, (247, 255, 0)
)

speed_x = 3
speed_y = 3

finish = False

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        
        window.fill(back)

        kot.rect.x += speed_x
        kot.rect.y += speed_y
        if sprite.collide_rect(right_fighter, kot) or sprite.collide_rect(left_fighter, kot):
            speed_x *= -1
            speed_y *= 1

        if kot.rect.x < 0:
            finish = True
            window.blit(leftlose, (200, 200))

        if kot.rect.x > 700:
            finish = True
            window.blit(rightlose, (200, 200))

        if kot.rect.y > 450:
            speed_y *= -1

        if kot.rect.y < 0:
            speed_y *= -1

        kot.reset()
        right_fighter.reset()
        left_fighter.reset()

        left_fighter.updateL()
        right_fighter.updateR()

    clock.tick(FPS)
    display.update()