
# Import and initialize pygame
import pygame
pygame.init()
# Configure the screen
screen = pygame.display.set_mode([500, 500])

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

# instance of GameObject
apple = GameObject(120, 300, 'apple.png')
strawberry = GameObject(350, 350, 'strawberry.png')

# Creat the game loop
running = True
while running:
  # Looks at events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      
  # Draw a circle
  screen.fill((255, 255, 255))
  #draw surface
  apple.render(screen)
  strawberry.render(screen)
  # Update the window
  pygame.display.flip()