
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

# Creat the game loop
running = True
while running:
  # Looks at events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      
  # Draw a circle
  screen.fill((255, 255, 255))
  #update the position
  apple.move()
  strawberry.move()
  #draw surface
  apple.render(screen)
  strawberry.render(screen)
  # Update the window
  pygame.display.flip()
  #tick the clock!
  clock.tick(60)