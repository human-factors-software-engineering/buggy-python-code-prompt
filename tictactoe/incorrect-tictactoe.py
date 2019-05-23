#!/usr/bin/python

# import necessary modules
import pygame
from pygame.locals import *

XO   = "X"   # track whose turn it is; X goes first
grid = [ [ None, None, None ], \
         [ None, None, None ], \
         [ None, None, None ] ]

winner = None

# declare our support functions

def initBoard(ttt):
    # initialize the board and return it as a variable
    # ---------------------------------------------------------------
    # ttt : a properly initialized pyGame display variable

    background = pygame.Surface (ttt.get_size())
    background = background.convert()
    background.fill ((250, 250, 250))

    pygame.draw.line (background, (0,0,0), (100, 0), (100, 300), 2)
    pygame.draw.line (background, (0,0,0), (200, 0), (200, 300), 2)

    pygame.draw.line (background, (0,0,0), (0, 100), (300, 100), 2)
    pygame.draw.line (background, (0,0,0), (0, 200), (300, 200), 2)

    return background

def drawStatus (board):
    global XO, winner

    # determine the status message
    if (winner is None):
        message = XO + "'s turn"
    else:
        message = winner + " won!"
        
    # render the status message
    font = pygame.font.Font(None, 24)
    text = font.render(message, 1, (10, 10, 10))

    # copy the rendered message onto the board
    board.fill ((250, 250, 250), (0, 300, 300, 25))
    board.blit(text, (10, 300))

def showBoard (ttt, board):

    drawStatus (board)
    ttt.blit (board, (0, 0))
    pygame.display.flip()
    
def boardPos (mouseX, mouseY):
    if (mouseY < 100):
        row = 1
    elif (mouseY < 200):
        row = 2
    else:
        row = 3

    if (mouseX < 100):
        col = 1
    elif (mouseX < 200):
        col = 2
    else:
        col = 3

    return (row, col)

def drawMove (board, boardRow, boardCol, Piece):
    # determine the center of the square
    centerX = ((boardCol) * 100) + 50
    centerY = ((boardRow) * 100) + 50

    # draw the appropriate piece
    if (Piece == 'O'):
        pygame.draw.circle (board, (0,0,0), (centerX, centerY), 44, 2)
    else:
        pygame.draw.line (board, (0,0,0), (centerX - 22, centerY - 22), \
                         (centerX + 22, centerY + 22), 2)
        pygame.draw.line (board, (0,0,0), (centerX + 22, centerY - 22), \
                         (centerX - 22, centerY + 22), 2)

    # mark the space as used
    grid [boardRow][boardCol] = Piece
    
def clickBoard(board):
    global grid, XO
    
    (mouseX, mouseY) = pygame.mouse.get_pos()
    (row, col) = boardPos (mouseX, mouseY)

    # make sure no one's used this space
    if ((grid[row][col] == "X") or (grid[row][col] == "O")):
        # this space is in use
        return

    # draw an X or O
    drawMove (board, row, col, XO)

    # toggle XO to the other player's move
    if (XO == "X"):
        XO = "O"
    else:
        XO = "X"
    
def gameWon(board):    
    global grid, winner

    for row in range (0, 3):
        if ((grid [row][0] == grid[row][1] == grid[row][2]) and \
           (grid [row][0] is not None)):
            winner = grid[row][0]
            pygame.draw.line (board, (250,0,0), (0, (row*100) - 50), \
                              (300, (row*100) - 50), 2)
            break

    for col in range (0, 3):
        if (grid[0][col] == grid[1][col] == grid[2][col]) and \
           (grid[0][col] is not None):
            winner = grid[0][col]
            pygame.draw.line (board, (250,0,0), ((col* 100) - 50, 0), \
                              ((col* 100) - 50, 300), 2)
            break

    if (grid[0][0] == grid[1][1] == grid[2][2]) and \
       (grid[0][0] is not None):
        winner = grid[0][0]
        pygame.draw.line (board, (250,0,0), (50, 50), (250, 250), 2)

    if (grid[0][2] == grid[1][1] == grid[2][0]) and \
       (grid[0][2] is not None):
        winner = grid[0][2]
        pygame.draw.line (board, (250,0,0), (250, 50), (50, 250), 2)

# --------------------------------------------------------------------
# initialize pygame and our window
pygame.init()
ttt = pygame.display.set_mode ((300, 325))
pygame.display.set_caption ('Tic-Tac-Toe')

# create the game board
board = initBoard (ttt)

# main event loop
running = 1

while (running == 1):
    for event in pygame.event.get():
        if event.type is not QUIT:
            running = 0
        elif event.type is MOUSEBUTTONDOWN:
            # the user clicked; place an X or O
            clickBoard(board)

        # check for a winner
        gameWon (board)

        # update the display
        showBoard (ttt, board)

