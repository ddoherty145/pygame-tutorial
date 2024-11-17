import pygame 
pygame.init()

#confirm screen size
screen = pygame.display.set_mode([500, 500])

#define colors
red = (255, 59, 48)
orange = (255, 149, 0)
yellow = (255, 204, 0)
green = (76, 217, 100)
blue = (0, 122, 255)

#positions 
positions = [
    (150, 150), #red circle
    (350, 150), #organge circle
    (250, 250), #yellow circle
    (150, 350), #green circle
    (350, 350) #blue circle
]

radius = 50 #circle radius

#game loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #clear the screen
    screen.fill((255, 255, 255))
    #draw circle
    pygame.draw.circle(screen, red, positions[0], radius)
    pygame.draw.circle(screen, orange, positions[1], radius)
    pygame.draw.circle(screen, yellow, positions[2], radius)
    pygame.draw.circle(screen, green, positions[3], radius)
    pygame.draw.circle(screen, blue, positions[4], radius)
    # update display
    pygame.display.flip()

pygame.quit()