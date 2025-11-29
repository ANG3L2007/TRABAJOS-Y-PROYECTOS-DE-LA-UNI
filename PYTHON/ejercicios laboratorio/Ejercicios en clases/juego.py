import pygame



# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 750))
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("green")
    #imprima en consola help(pygame.draw)
    pygame.draw.line(screen, "yellow",[0,0],[200,500],5)
    pygame.draw.line(screen, "red",[200,500],[200,720],5)
    pygame.draw.line(screen, "blue",[200,720],[400,720],5)
    
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60
