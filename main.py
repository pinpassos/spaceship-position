# Import modules
import pygame

# Color and size
(width, height) = (600, 450)
background_color = (255, 255, 255)

# Screen config
screen = pygame.display.set_mode((width, height)) # Screen size
screen.fill(background_color) # Background color screen
pygame.display.set_caption('Pygame Screen') # Title screen

spaceship = pygame.image.load('images\spaceship.png') # Spaceship image
spaceship_X = 0
spaceship_Y = 350

pygame.font.init() 
myfont = pygame.font.SysFont('Arial', 30)
textsurface = myfont.render('Inital position', False, (0, 0, 0))

def player(x, y):
    screen.blit(spaceship, (x, y))

pygame.display.flip() # Start screen
    
# Main
game = True
while game:

    screen.fill(background_color)
    textPosition = myfont.render(f'X: {spaceship_X} | Y: {spaceship_Y}', False, (0, 0, 0))
    
    # Stop game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
    # Pressed keys for movements
    commands = pygame.key.get_pressed()

    if commands[pygame.K_UP]:
        if spaceship_Y <= 0:
            spaceship_Y = 0
            textsurface = myfont.render('Min top position', False, (0, 0, 0))
        else:
            spaceship_Y -= 1
            
    if commands[pygame.K_DOWN]:
        if spaceship_Y >= 380:
            spaceship_Y = 380
            textsurface = myfont.render('Max bottom position', False, (0, 0, 0))
        else:
            spaceship_Y += 1
        
    if commands[pygame.K_LEFT]:
        if spaceship_X <= 0:
            spaceship_X = 0
            textsurface = myfont.render('Min left position', False, (0, 0, 0))
        else:
            spaceship_X -= 1

    if commands[pygame.K_RIGHT]:
        if spaceship_X >= 530:
            spaceship_X = 530
            textsurface = myfont.render('Max right position', False, (0, 0, 0))
        else:
            spaceship_X += 1
            
    # Draw images on screen
    player(spaceship_X, spaceship_Y)
    screen.blit(textsurface,(220,200))
    screen.blit(textPosition,(220, 160))
    pygame.display.update()