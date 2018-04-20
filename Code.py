import pygame,sys,random
from pygame.locals import *

FPS = 50
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((1000,800),0,32)
pygame.display.set_caption('pygame window')

BLACK = (0,0,0)
WHITE = (255,255,255)

up = False
down = False
left = False
right = False
superUp = False
superDown = False
won = False
count = 0

class Player(pygame.sprite.Sprite):
  def __init__(self,image,x,y):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load(image)
    self.rect = self.image.get_rect(x=x, y=y)
class flagMake(pygame.sprite.Sprite):
  def __init__(self,image,x,y):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load(image)
    self.size = self.image.get_size()
    self.smaller_img = pygame.transform.scale(self.image,
(int(self.size[0]),int(self.size[1])))
    self.rect = self.image.get_rect(x=x, y=y)

blockMinWidth,blockMaxWidth = 200,600

for i in range (0,100):
  gap1X = random.randint(10,950)
  gap1Width = random.randint(blockMinWidth,blockMaxWidth)
  gap1W = gap1X + gap1Width

  gap2X = random.randint(10,950)
  gap2Width = random.randint(blockMinWidth,blockMaxWidth)
  gap2W = gap2X + gap2Width

  gap3X = random.randint(10,950)
  gap3Width = random.randint(blockMinWidth,blockMaxWidth)
  gap3W = gap3X + gap3Width
  won = False
  flag = flagMake('gem5.png',0,0)#########on Block Three ####### )
  player1 = Player('cat.png',10,655)
  players = pygame.sprite.Group(player1,flag)
  finish = pygame.sprite.Group(flag)
  while won == False:
    DISPLAYSURF.fill(WHITE)
    floor = pygame.draw.polygon(DISPLAYSURF,BLACK,((1000,730),(0,730),(0,800),(1000,800)))
    #floor is y = 655

    block1a = pygame.draw.polygon(DISPLAYSURF,BLACK,((1000,530),(gap1W,530),(gap1W,600),(1000,600)))
    block1b = pygame.draw.polygon(DISPLAYSURF,BLACK,((gap1X,530),(0,530),(0,600),(gap1X,600)))

    block2a = pygame.draw.polygon(DISPLAYSURF,BLACK,((1000,330),(gap2W,330),(gap2W,400),(1000,400)))
    block2b = pygame.draw.polygon(DISPLAYSURF,BLACK,((gap2X,330),(0,330),(0,400),(gap2X,400)))

    block3a = pygame.draw.polygon(DISPLAYSURF,BLACK,((1000,130),(gap3W,130),(gap3W,200),(1000,200)))
    block3b = pygame.draw.polygon(DISPLAYSURF,BLACK,((gap3X,130),(0,130),(0,200),(gap3X,200)))

    block1Top = block1a.top
    block1Bottom = block1a.bottom
    block2Bottom = block2a.bottom
    block3Bottom = block3a.bottom

    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == KEYDOWN:
        if event.key == K_LEFT or event.key == K_a:
          left = True
        if event.key == K_RIGHT or event.key == K_d:
          right = True
        if event.key == K_DOWN or event.key == K_s:
          down = True
        if event.key == K_UP or event.key == K_w:
          up = True
        if event.key == K_z:
          superUp = True
        if event.key == K_x:
          superDown = True
      elif event.type == KEYUP:
        if event.key == K_LEFT or event.key == K_a:
          left = False
        if event.key == K_RIGHT or event.key == K_d:
          right = False
        if event.key == K_DOWN or event.key == K_s:
          down = False

    if player1.rect.colliderect(floor) == False and player1.rect.colliderect(block1a) == False and player1.rect.colliderect(block2a) == False and player1.rect.colliderect(block3a) == False and player1.rect.colliderect(block1b) == False and player1.rect.colliderect(block2b) == False and player1.rect.colliderect(block3b) == False and up == False and down == False:
      down = True
    if player1.rect.colliderect(flag) == True:
      won = True

    if player1.rect.colliderect(block1a) == True or player1.rect.colliderect(block1b) == True:
      if down == True:
         down = False
         player1.rect.y = 452
      elif player1.rect.y == block1Bottom or player1.rect.y == block1Bottom -1 or player1.rect.y == block1Bottom -2 or player1.rect.y == block1Bottom -3 or player1.rect.y == block1Bottom -4 or player1.rect.y == block1Bottom -5 :
         up = False
         player1.rect.y = 602
         down = True

    if player1.rect.colliderect(block2a) == True or player1.rect.colliderect(block2b) == True:
       if down == True:
          down = False
          player1.rect.y = 252
       elif player1.rect.y == block2Bottom or player1.rect.y == block2Bottom -1 or player1.rect.y == block2Bottom -2 or player1.rect.y == block2Bottom -3 or player1.rect.y == block2Bottom -4 or player1.rect.y == block2Bottom -5 :
          up = False
          player1.rect.y = 402
          down = True

    if player1.rect.colliderect(block3a) == True or player1.rect.colliderect(block3b) == True:
       if down == True:
          down = False
          player1.rect.y = 52
       elif player1.rect.y == block3Bottom or player1.rect.y == block3Bottom -1 or player1.rect.y == block3Bottom -2 or player1.rect.y == block3Bottom -3 or player1.rect.y == block3Bottom -4 or player1.rect.y == block3Bottom -5 :
          up = False
          player1.rect.y = 202
          down = True


    if player1.rect.colliderect(floor) == True:
       if down == True:
          down = False
          player1.rect.y = 655
       if superDown == True:
          superDown = False
          player1.rect.y = 655

    if left == True:
      player1.rect.move_ip(-10,0)
    if right == True:
      player1.rect.move_ip(10,0)
    if up == True:
      player1.rect.move_ip(0,-15)
      count += 1
      if count >= 20:
        up = False
        count = 0
    if superUp == True:
      player1.rect.move_ip(0,-45)
      count += 1
      if count >= 8:
        superUp = False
        count = 0

    if superDown == True:
      player1.rect.move_ip(0,45)
      count += 1
      if count >= 8:
        superDown = False
        count = 0
    if down == True:
      if player1.rect.y >= 655:
        player1.rect.y = 655
      else:
        player1.rect.move_ip(0,1)

    if player1.rect.y <= 0:
      player1.rect.y = 1
    if player1.rect.y >= 700:
      player1.rect.y = 699
    if player1.rect.x <= 0:
      player1.rect.x = 1
    if player1.rect.x >= 879:
      player1.rect.x = 880


    players.draw(DISPLAYSURF)
    pygame.display.update()
    fpsClock.tick(FPS)
