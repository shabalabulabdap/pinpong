from pygame import *

class GameSprite(sprite.Sprite):
    def  __init__(self, player_image, player_x, player_y, width, height, player_speed):
        sprite.Sprite.__init__(self)
        self.image  = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
    
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height-80:
            self.rect.y += self.speed
    
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height-80:
            self.rect.y += self.speed

back = (200,255,255)
win_width = 700
win_height = 500
display.set_caption("ping-pong")
window = display.set_mode((win_width, win_height))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60
goals_player1 = 0
goals_player2 = 0
WIN_SCORE = 11

racket1 = Player("racket.png", 30,200, 50, 150, 4)
racket2 = Player("racket.png", 620,200, 50, 150, 4)
ball = GameSprite('tenis_ball.png', 350, 200, 50, 50, 4)

font.init()
font1 = font.SysFont("Arial", 35)
lose1 = font1.render("Player 1 LOST!!!!", True, (180, 0, 0))
lose2 = font1.render("Player 2 LOST!!!!", True, (180, 0, 0))

speed_x =3
speed_y=3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish == False:
        window.fill(back)

        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        statistics1 = font1.render(str(goals_player1), True, (0,0,0))
        statistics2 = font1.render(str(goals_player2), True, (0,0,0))

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1

        if ball.rect.y >win_height - 50 or  ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            goals_player2+= 1
            window.blit(lose1, (300, 200))  
            time.delay(1000)
        if ball.rect.x > win_width:
            goals_player1+=1
            finish = True
            window.blit(lose2, (300, 200))
            time.delay(1000)

        if goals_player1>=10 and goals_player2>=10:

            if abs(goals_player1 - goals_player2)==2:
                if goals_player1 > goals_player2:
                   print("PLAYER 1 WON")   
                if goals_player2 > goals_player1:
                    print("PLAYER 2 WON")
                finish = True

        if goals_player1 == WIN_SCORE:
            print("PLAYER 1 WON")
            finish = True
        elif goals_player2 == WIN_SCORE:
            print("PLAYER 2 WON")
            finish = True

        window.blit(statistics1, (35, 25))
        window.blit(statistics2, (win_width-35, 25))
        racket1.reset()
        racket2.reset()
        ball.reset()
    
    else:
        time.delay(2000)
        finish = False
        ball.rect.x = 350
        ball.rect.y = 200
        goals_player1 = 0
        goals_player2 = 0


    display.update()
    clock.tick(FPS)