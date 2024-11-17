import pygame 
pygame.init()

#confirm screen size
screen = pygame.display.set_mode([500, 500])

#game loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #clear the screen
    screen.fill((255, 255, 255))
    #draw circle
    color = (250, 141, 7)
    position = (250, 250)
    pygame.draw.circle(screen, color, position, 75)
    # update display
    pygame.display.flip()