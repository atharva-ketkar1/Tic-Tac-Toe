import pygame

# Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LINE_WIDTH = 4

# Draws the board lines
def draw_board(screen):
    screen.fill(BLACK)  

    for i in range(1, 3):
        pygame.draw.line(screen, WHITE, (0, i * 100), (300, i * 100), LINE_WIDTH) # Draws the horizontal white lines 
        pygame.draw.line(screen, WHITE, (i * 100, 0), (i * 100, 300), LINE_WIDTH) # Draws the vertical white lines 
