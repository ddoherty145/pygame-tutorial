
# Import and initialize pygame
import pygame
from random import randint, choice
pygame.init()

#background
background_image_path = 'firey_dungeon.png'
background = pygame.image.load(background_image_path)

image_width, image_height = background.get_size()
# Configure the screen
screen = pygame.display.set_mode([image_width, image_height])
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
fruit_sprites = pygame.sprite.Group()
lanes = [93, 218, 343]


class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
       super(GameObject, self).__init__()
       self.surf = pygame.image.load(image)
       self.x = x
       self.y = y
       self.rect = self.surf.get_rect()

    def render(self, screen):
        self.rect.x = self.x
        self.rect.y = self.y
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
        if self.x > 500 or self.x < -64:
            self.reset()

    def reset(self):
        self.y = choice(lanes)
        direction = choice([-1, 1])
        self.dx = direction * ((randint(1, 200)/ 100) + 1)
        if direction == -1:
            self.x = 500
        else:
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
        if self.y > 500 or self.y < -64:
            self.reset()

    def reset(self):
        self.x = choice(lanes)
        direction = choice([-1, 1])
        self.dy = direction * ((randint(1, 200)/ 100) + 1)
        if direction == -1:
            self.y = 500
        else:
            self.y = -64

class Bomb(GameObject):
    def __init__(self):
        super(Bomb, self).__init__(0, 0, 'bomb.png')
        self.dx = 0
        self.dy = 0
        self.reset()

    def move(self):
        self.x += self.dx
        self.y += self.dy

        if self.x < -64 or self.x > 500 or self.y < -64 or self.y > 500:
            self.reset()

    def reset(self):
        self.x = choice(lanes)
        self.y = choice(lanes)

        direction = choice(['up', 'down', 'left', 'right'])
        speed = (randint(1, 200) / 100) + 1

        if direction == 'up':
            self.dx = 0
            self.dy = -speed
            self.y = 500  # Start at the bottom
        elif direction == 'down':
            self.dx = 0
            self.dy = speed
            self.y = -64  # Start at the top
        elif direction == 'left':
            self.dx = -speed
            self.dy = 0
            self.x = 500  # Start at the right edge
        elif direction == 'right':
            self.dx = speed
            self.dy = 0
            self.x = -64  # Start at the left edge


# instance of GameObject
apple = Apple()
strawberry = Strawberry()
player = Player()
bomb = Bomb()
#adding sprites to all_sprites
all_sprites.add(player)
all_sprites.add(apple)
all_sprites.add(strawberry)
all_sprites.add(bomb)
fruit_sprites.add(apple)
fruit_sprites.add(strawberry)
#define score
score = 0
#font for score 
pygame.font.init()
font = pygame.font.SysFont(None, 32)
#display font
def display_score():
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

#lives
lives = 3
heart_image = pygame.image.load('heart.png')

def display_lives():
    for i in range(lives):
        screen.blit(heart_image, (10 + i * 40, 40))

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
      
  screen.blit(background, (0, 0))
  
  #move and render sprites
  for entity in all_sprites:
        entity.move()
        entity.render(screen)

  fruit = pygame.sprite.spritecollideany(player, fruit_sprites)
  if fruit:
        score += 1
        fruit.reset()

  if pygame.sprite.collide_rect(player, bomb):
    lives -= 1
    if lives <= 0:
        running = False
    else:
        player.reset()

  display_score()
  display_lives()
        
  # Update the window
  pygame.display.flip()
  #tick the clock!
  clock.tick(60)