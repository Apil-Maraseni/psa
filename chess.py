#create a simple chess game with a board and pieces working fully with Pygame
import pygame
from pygame.locals import *
from PIL import Image, ImageDraw, ImageFont
import os

os.makedirs('images', exist_ok=True)
pieces = ['pawn', 'rook', 'knight', 'bishop', 'queen', 'king']
colors = ['white', 'black']
def create_piece_image(piece, color):
    image = Image.new('RGBA', (100, 100), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    draw.text((10, 10), f"{color} {piece}", fill=(0, 0, 0), font=font)
    image.save(f'images/{color}_{piece}.png')
for color in colors:
    for piece in pieces:
        create_piece_image(piece, color)


class ChessGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Chess Game")
        self.clock = pygame.time.Clock()
        self.running = True
        self.board = self.create_board()
        self.load_images()

    def create_board(self):
        return [[None for _ in range(8)] for _ in range(8)]

    def load_images(self):
        self.images = {}
        pieces = ['pawn', 'rook', 'knight', 'bishop', 'queen', 'king']
        colors = ['white', 'black']
        for color in colors:
            for piece in pieces:
                image_path = f'images/{color}_{piece}.png'
                self.images[f'{color}_{piece}'] = pygame.image.load(image_path).convert_alpha()
        self.images['white_pawn'] = pygame.transform.scale(self.images['white_pawn'], (100, 100))
        self.images['black_pawn'] = pygame.transform.scale(self.images['black_pawn'], (100, 100))   
        self.images['white_rook'] = pygame.transform.scale(self.images['white_rook'], (100, 100))
        self.images['black_rook'] = pygame.transform.scale(self.images['black_rook'], (100, 100))
        self.images['white_knight'] = pygame.transform.scale(self.images['white_knight'], (100, 100))
        self.images['black_knight'] = pygame.transform.scale(self.images['black_knight'], (100, 100))
        self.images['white_bishop'] = pygame.transform.scale(self.images['white_bishop'], (100, 100))
        self.images['black_bishop'] = pygame.transform.scale(self.images['black_bishop'], (100, 100))
        self.images['white_queen'] = pygame.transform.scale(self.images['white_queen'], (100, 100))
        self.images['black_queen'] = pygame.transform.scale(self.images['black_queen'], (100, 100))
        self.images['white_king'] = pygame.transform.scale(self.images['white_king'], (100, 100))
        self.images['black_king'] = pygame.transform.scale(self.images['black_king'], (100, 100))
        self.images['empty_square'] = pygame.Surface((100, 100))
        self.images['empty_square'].fill((255, 255, 255))
        for key in self.images:
            if self.images[key].get_size() != (100, 100):
                self.images[key] = pygame.transform.scale(self.images[key], (100, 100))
                self.images[key].set_colorkey((255, 255, 255))
                self.images[key] = self.images[key].convert_alpha()
                

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
            self.screen.fill((255, 255, 255))
            self.draw_board()
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()

    def draw_board(self):
        for row in range(8):
            for col in range(8):
                color = (255, 255, 255) if (row + col) % 2 == 0 else (0, 0, 0)
                pygame.draw.rect(self.screen, color, (col * 100, row * 100, 100, 100))
                piece = self.board[row][col]
                if piece:
                    self.screen.blit(self.images[piece], (col * 100, row * 100))
    def place_piece(self, piece, row, col):
        if 0 <= row < 8 and 0 <= col < 8:
            self.board[row][col] = piece
    def move_piece(self, start_row, start_col, end_row, end_col):
        if 0 <= start_row < 8 and 0 <= start_col < 8 and 0 <= end_row < 8 and 0 <= end_col < 8:
            piece = self.board[start_row][start_col]
            if piece:
                self.board[end_row][end_col] = piece
                self.board[start_row][start_col] = None
    def reset_board(self):
        self.board = self.create_board()
        self.load_images()

if __name__ == "__main__":
    game = ChessGame()
    game.place_piece('white_pawn', 1, 0)
    game.place_piece('black_rook', 7, 0)
    game.run()

# Note: Ensure you have the images in the 'images' directory with the correct naming convention.
# The images should be named as 'white_pawn.png', 'black_rook.png', etc.
# This code creates a simple chess game with a graphical interface using Pygame.
# You can place pieces on the board and move them around.
# Make sure to have Pygame installed in your Python environment.