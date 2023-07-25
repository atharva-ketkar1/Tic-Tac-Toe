import pygame
import sys
from board import draw_board

pygame.init()

COLS, ROWS = 3, 3
CROSS_PAD = 15 # Extra padding for the X not to touch the sides 
LINE_PAD = 4 # Extra padding for the line 
WHITE = (255, 255, 255) 

# Create the screen
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Tic Tac Toe")

# Function to display the initial blank board
def show_blank_board():
    draw_board(screen)
    pygame.display.update()

# Mark the empty board with " "
board = []
for row in range(ROWS):
    row_list = []
    for col in range(COLS):
        row_list.append(" ")
    board.append(row_list)

# Function to draw the X 
def draw_x(screen, row, col):
    x_left = col * 100 + CROSS_PAD 
    x_right = (col + 1) * 100 - CROSS_PAD
    y_top = row * 100 + CROSS_PAD
    y_bottom = (row + 1) * 100 - CROSS_PAD
    pygame.draw.line(screen, WHITE, (x_left, y_top), (x_right, y_bottom), LINE_PAD)
    pygame.draw.line(screen, WHITE, (x_left, y_bottom), (x_right, y_top), LINE_PAD)

# Function to draw the O
def draw_o(screen, row, col):
    x_center = col * 100 + 50
    y_center = row * 100 + 50
    pygame.draw.circle(screen, WHITE, (x_center, y_center), 40, LINE_PAD)

 # Function to place the figures on the board   
def draw_figures():
    for row in range(ROWS):
        for col in range(COLS):
            symbol = board[row][col]
            if symbol == "X":
                draw_x(screen, row, col)
            elif symbol == "O":
                draw_o(screen, row, col)


# Function to mark the square when user clicks
def mark_square(row, col, player):
    board[row][col] = player

# Function to check for three in a row
def check_win(player):
    # Check rows and columns
    if any(all(board[i][j] == player for j in range(COLS)) or
           all(board[j][i] == player for j in range(COLS)) for i in range(ROWS)):
        return True

    # Check main diagonal
    if all(board[i][i] == player for i in range(ROWS)):
        return True

    # Check secondary diagonal
    if all(board[i][ROWS - i - 1] == player for i in range(ROWS)):
        return True

    return False


# Function to check if the board is full
def is_board_full():
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == " ":
                return False
    return True

def main():
    player = "X"

    show_blank_board()

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = event.pos
                col = mouseX // 100
                row = mouseY // 100

                if board[row][col] == " ":
                    mark_square(row, col, player)
                    if check_win(player):
                        game_over = True
                        print(f"Player {player} wins")
                    elif is_board_full():
                        game_over = True
                        print("It's a tie")
                    else:
                        if player == "O":
                            player = "X"
                        else:
                            player = "O"

        # Draw the board
        draw_board(screen)
        draw_figures()

        pygame.display.update()

if __name__ == "__main__":
    main()
