import pygame
from sys import exit


def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = test_font.render(f'Score: {current_time}', False, (64, 64, 64))
    score_rectangle = score_surface.get_rect(center=(400, 50))
    screen.blit(score_surface, score_rectangle)
    return current_time


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
# Gives us a clock object
clock = pygame.time.Clock()
#  Creates a font to use in making text, Step 1 of displaying text on the screen
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0

# Loads in an image. In PyCharm this was really easy,
# As long as the files are in the same location as you .py file.
# The covert is used to make the image easier for python to work with.
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
# This creates a text surface, taking in the font, Anti-aliasing(boolean), and a color
# This is step 2 of rending text to the screen
# score_surface = test_font.render('My game', False, (64, 64, 64))
# score_rectangle = score_surface.get_rect(midtop=(400, 50))
# This adds a snail image
# You need convert alpha here to avoid a white background on the snail
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
# This creates a positional variable we can manipulate to move the position of the snail image
snail_rectangle = snail_surface.get_rect(midbottom=(600, 300))

# Creates the player surface, gives it an image
# Then draws a rectangle around it by using get_rect()
# The Rectangle then allows you to position the image
# In the scene easier by choosing where you base the location from
# Example  being either bottommiddle, topleft, topright, and so on.
player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom=(80, 300))
player_gravity = 0
# Intro Screen
player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rectangle = player_stand.get_rect(center=(400, 200))


game_name = test_font.render('Pixel Runner', False, (111, 196, 169))
game_name_rectangle = game_name.get_rect(center=(400, 80))

game_message = test_font.render('Press space to run', False, (111, 196, 169))
game_message_rectangle = game_message.get_rect(center=(400, 330))
# This creates a surface, which goes over the display surface.
# It takes a size for the surface to be.
# NOTE: THESE ARE NOT THE LOCATION OF THE SURFACE
# JUST THE SIZE OF THE SURFACE
# test_surface = pygame.Surface((100, 200))
# This fills the surface  with red so we can see it's location.
# test_surface.fill('Red')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rectangle.collidepoint(event.pos) and player_rectangle.bottom >= 300:
                    player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rectangle.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rectangle.left = 800

    # This is how we actually place the newly created surface in to the screen surface.
    # Remember, first number is width, second number height
    # And it starts 0 , 0 from the top left corner
    # Further note: They layer with the first called blit being the background
    # and then the second called blit layers on top of the 1st blit
    # and so on...
    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        # pygame.draw.rect(screen, '#c0e8ec', score_rectangle)
        # pygame.draw.rect(screen, '#c0e8ec', score_rectangle, 10)
        # screen.blit(score_surface, score_rectangle)

        score = display_score()

        # This increments snail position which is updated everytime the while loop runs
        # Which makes the image move across the screen to the right if positive
        # and to the left if negative. The if will reset the snails x pos
        # if it goes below the screen width/off the screen to the left
        snail_rectangle.x -= 4
        if snail_rectangle.right <= 0:
            snail_rectangle.left = 800
        screen.blit(snail_surface, snail_rectangle)
        # This is how the rectangle gets assigned to the player surface,
        # The Player surface will now be located where the rectangle is
        # This let's us move both objects as one by manipulation of the rect
        # Player
        player_gravity += 1
        player_rectangle.y += player_gravity
        if player_rectangle.bottom >= 300:
            player_rectangle.bottom = 300
        screen.blit(player_surface, player_rectangle)

        # collisions
        if snail_rectangle.colliderect(player_rectangle):
            game_active = False
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rectangle)
        start_time = int(pygame.time.get_ticks() / 1000)
        score_message = test_font.render(f'Your score: {score}', False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center=(400, 330))
        screen.blit(game_name, game_name_rectangle)

        if score == 0:
            screen.blit(game_message, game_message_rectangle)
        else:
            screen.blit(score_message, score_message_rect)
    pygame.display.update()
    # Tell the game not to run this loop faster than 60 times a second to control frame-rate
    clock.tick(60)
