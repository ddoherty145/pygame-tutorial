
# Import and initialize pygame
import pygame
from random import randint, choice
pygame.init()
# Configure the screen
screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
lanes = [93, 218, 343]

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
        self.pos_x = 1
        self.pos_y = 1
        self.reset()

    def left(self):
        if self.pos_x > 0:
            self.pos_x -= 1
            self.update_dx_dy()

    def right(self):
        if self.pos_x < len(lanes) - 1:
            self.pos_x += 1
            self.update_dx_dy()

    def up(self):
        if self.pos_y > 0:
            self.pos_y -= 1
            self.update_dx_dy()

    def down(self):
        if self.pos_y < len(lanes) - 1:
            self.pos_y += 1
            self.update_dx_dy()

    def move(self):
        self.x -= (self.x - self.dx) * 0.25
        self.y -= (self.y - self.dy) * 0.25

        self.x = max(0, min(self.x, 500 - 64))
        self.y = max(0, min(self.y, 500 - 64))

    def update_dx_dy(self):
        self.dx = lanes[self.pos_x]
        self.dy = lanes[self.pos_y]

    def reset(self):
        self.x = lanes[self.pos_x]
        self.y = lanes[self.pos_y]
        self.dx = self.x
        self.dy = self.y

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
        self.y = choice(lanes)
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
        self.x = choice(lanes)
        self.y = -64

# instance of GameObject
apple = Apple()
strawberry = Strawberry()
player = Player()
#adding sprites to all_sprites
all_sprites.add(player)
all_sprites.add(apple)
all_sprites.add(strawberry)

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
  
  #move and render sprites
  for entity in all_sprites:
        entity.move()
        entity.render(screen)
  # Update the window
  pygame.display.flip()
  #tick the clock!
  clock.tick(60)