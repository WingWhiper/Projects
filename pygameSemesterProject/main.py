import pygame


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Battleship Game')
clock = pygame.time.Clock()
game_active = True
background = pygame.image.load('images/BG.png').convert()
header_font = pygame.font.SysFont('blackadderitc', 25)
side_font = pygame.font.SysFont('timesnewroman', 10)
# Create a variable to edit the header area text
game_name = header_font.render('A battleship game', False, (0, 0, 0))
game_name_rect = game_name.get_rect(center=(400, 25))
# create a variable to hold the right side display text
side_display_text = side_font.render('Remaining ships', False, (0, 0, 0))
side_display_text_rect = side_display_text.get_rect(center=(750, 105))

# Testing ways to get rectangles around squares, or atleast blit something to that square
# black_box = pygame.draw.rect(screen, (0, 0, 0), (65, 50))
# black_box_rect = black_box.get_rect(topleft=(4, 54))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if game_active:
        screen.blit(background, (0, 0))
        screen.blit(game_name, game_name_rect)
        screen.blit(side_display_text, side_display_text_rect)
        # screen.blit(black_box, black_box_rect)

    pygame.display.update()
    clock.tick(60)
