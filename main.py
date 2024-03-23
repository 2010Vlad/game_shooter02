from pygame import *
import sys
from random import randint
window = display.set_mode((700, 500))
display.set_caption("Лабиринт")
#background = transform.scale(image.load("background.jpg"), (700, 500))

mixer.init()
mixer.music.load('seday.mp3')
mixer.music.play()
clock = time.Clock()
#damage = mixer.Sound("zvyk gg.mp3")
#finish = mixer.Sound("fru.mp3")

#fru = mixer.Sound("fru.mp3")
font.init()
font = font.Font(None, 70)
win = font.render("Браво", True,(0,255,0 ))
lose = font.render("Я не удивлен", True,(255,0,0))


FPS = 60
game = True
class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed,player_size_x, player_size_y):
      super().__init__()
      self.image = transform.scale(image.load(player_image), (player_size_x, player_size_y))
      self.speed = player_speed
      self.rect = self.image.get_rect()
      self.rect.x = player_x
      self.rect.y = player_y
   def reset(self):
      window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
   def update(self):
      key_pressed = key.get_pressed()
      if key_pressed[K_w] and self.rect.y > 0:
         self.rect.y -= self.speed
      if key_pressed[K_s] and self.rect.y < 450:
         self.rect.y += self.speed
      if key_pressed[K_a] and self.rect.x > 0:
         self.rect.x -= self.speed
      if key_pressed[K_d] and self.rect.x < 650:
         self.rect.x += self.speed

class Enemy(GameSprite):
   direct = "left"
   def update(self):
      if self.rect.x <= 400:
         self.direct = "right"
      if self.rect.x >= 600:
         self.direct = "left"
      if self.direct == "left":
         self.rect.x -= self.speed
      else:
         self.rect.x += self.speed
class Wall(sprite.Sprite):
   def __init__(self, color1, color2, color3, wall_x, wall_y, wall_w, wall_h):
      super().__init__()
      self.color1 = color1
      self.color2 = color2
      self.color3 = color3
      self.wall_w = wall_w
      self.wall_h = wall_h
      self.image = Surface((wall_w, wall_h))
      self.image.fill((color1,color2,color3))
      self.rect = self.image.get_rect()
      self.rect.x = wall_x
      self.rect.y = wall_y
   def draw_wall(self):
      window.blit(self.image, (self.rect.x, self.rect.y))

class EnemyNew(GameSprite):
    def update(self):
        self.rect.x -= self.speed
        if self.rect.x <= 10:
            #self.rect.y =  randint(50, win_height-200)
            #self.rect.x = randint(100, win_width-500
            self.rect.y = randint(50, win_width-50)
            self.rect.x = 700
def fire(self):
   bullet = Bullet("pyli.png", self.rect.centerx, self.rect.top, 10, 20, 10)
   bullets.add(bullet)
       #bullet
class Bullet(GameSprite):
    def update(self):
        self.rect.x -= self.speed
        if self.rect.y <= 0:
            self.kill()
bullets = sprite.Group()
#w1(154, 205, 50,100, 20, 450, 10)
#w2(154, 205, 50, 100, 480, 350, 10)
#w3(154,205, 50, 100, 20, 10, 380)


win_width = 700
win_height = 500

background = GameSprite('background.jpg', 0,0,0,700,500)
hero = Player('sp2.png', 0,10,5,70,80)
enemy = Enemy('sp1.png', 400,300,5,100,100)
gold = GameSprite('gelyd.png',600,400,0,100,100)
w1 = Wall(255, 255, 218, 100, 20, 340, 10)
w2 = Wall(255, 255, 218,250, 150, 200, 10)
w3 = Wall(255, 255, 218, 100, 20, 10,380 )
w4 = Wall(255, 255, 218, 450, 150, 10, 380)
w5 = Wall(255, 255, 218, 240, 150, 10, 380)
#enemy2 = EnemyNew("sp1.png", randint(50, win_width-500),10,5,50,50)
for i in range(20):
   enemy2 = EnemyNew('sp1.png', 10,randint(50, win_width-500),5,50,50)


while game:
   for e in event.get():
      if e.type == QUIT:
         game = False

   background.reset()
   hero.update()
   hero.reset()
   enemy.update()
   enemy.reset()
   enemy2.update()
   enemy2.reset()
   gold.reset()
   w1.draw_wall()
   bullets.draw(window)
   bullets.update()
   w2.draw_wall()
   w3.draw_wall()
   w4.draw_wall()
   w5.draw_wall()
   if sprite.collide_rect(hero, gold):
      window.blit(win, (200,200))
      #finish.play()
      sys.exit()
   if sprite.collide_rect(hero, enemy) or sprite.collide_rect(hero, w1) or sprite.collide_rect(hero, w2) or sprite.collide_rect(hero, w3) or sprite.collide_rect(hero, w4) or sprite.collide_rect(hero, w5) or sprite.collide_rect(hero, enemy2):
      window.blit(lose, (200,200))
      #damage.play()
      hero.rect.x = 0
      hero.rect.y = 10


   display.update()
   clock.tick(FPS)