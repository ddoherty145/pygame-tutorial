
# Import and initialize pygame
import pygame
from random import randint
pygame.init()
# Configure the screen
screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()

class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
       super(GameObject, self).__init__()
    #    self.surf = pygame.Surface((width, height))
    #    self.surf.fill((255, 0, 255))
       self.surf = pygame.image.load(image)
       self.x = x
       self.y = y

    def render(self, screen):
        screen.blit(self.surf, (self.x, self.y))

class Player(GameObject):
    def __init__(self):
        super(Player, self).__init__(0, 0, 'player.png')
        self.dx = 0
        self.dy = 0
        self.reset()

    def left(self):
        self.dx -= 100

    def right(self):
        self.dx += 100

    def up(self):
        self.dy -= 100

    def down(self):
        self.dy += 100

    def move(self):
        self.x -= (self.x - self.dx) * 0.25
        self.y -= (self.y - self.dy) * 0.25

    def reset(self):
        self.x = 250 - 32
        self.y = 250 - 32

class Strawberry(GameObject):
    def __init__(self):
        super(Strawberry, self).__init__(0, 0, 'strawberry.png')
        self.dy = 0
        self.dx = (randint(1, 200)/ 100) + 1
        self.reset()

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x > 500:
            self.reset()

    def reset(self):
        self.y = randint(50, 400)
        self.x = -64


class Apple(GameObject):
    def __init__(self):
        super(Apple, self).__init__(0, 0, 'apple.png')
        self.dx = 0
        self.dy = (randint(1, 200)/ 100) + 1
        self.reset()

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.y > 500:
            self.reset()

    def reset(self):
        self.x = randint(50, 400)
        self.y = -64

# instance of GameObject
apple = Apple()
strawberry = Strawberry()
player = Player()

# Creat the game loop
running = True
while running:
  # Looks at events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            running = False
        elif event.key == pygame.K_LEFT:
            player.left()
        elif event.key == pygame.K_RIGHT:
            player.right()
        elif event.key == pygame.K_UP:
            player.up()
        elif event.key == pygame.K_DOWN:
            player.down()
      
  # Draw a circle
  screen.fill((255, 255, 255))
  #update the position
  apple.move()
  strawberry.move()
  player.move()
  #draw surface
  player.render(screen)
  apple.render(screen)
  strawberry.render(screen)
  # Update the window
  pygame.display.flip()
  #tick the clock!
  clock.tick(60)