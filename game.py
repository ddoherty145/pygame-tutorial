
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

# load imgaes
apple_image= 'apple.png'
strawberry_image = 'strawberry.png'

# list to store game objects
objects = []

# nested loop
fruit_positions = [
    [apple_image, strawberry_image, apple_image],
    [strawberry_image, apple_image, strawberry_image],
    [apple_image, strawberry_image, apple_image]
]

start_x, start_y = 100, 100
spacing = 150

for row in range(3):
    for col in range(3):
        x = start_x + col * spacing
        y = start_y + row * spacing
        image = fruit_positions[row][col]
        objects.append(GameObject(x, y, image))

# Creat the game loop
running = True
while running:
  # Looks at events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      
  # Draw a circle
  screen.fill((255, 255, 255))
  #render all objects
  for obj in objects:
    obj.render(screen)
  # Update the window
  pygame.display.flip()