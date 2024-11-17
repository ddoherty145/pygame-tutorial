import pygame 
pygame.init()

#confirm screen size
screen = pygame.display.set_mode([500, 500])

#define colors & radius
dark_grey = (50, 50, 50)
radius = 50

#spacing
spacing = 150
offset = 75

#game loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #clear the screen
    screen.fill((255, 255, 255))
    #nested loops to draw the circles
    for row in range(3):
        for col in range(3):
            x = offset + col * spacing
            y = offset + row * spacing
            pygame.draw.circle(screen, dark_grey, (x, y), radius)
    # update display
    pygame.display.flip()

pygame.quit()