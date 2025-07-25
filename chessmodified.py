import pygame
from pygame.locals import *
from PIL import Image, ImageDraw, ImageFont
import os

# Setup
os.makedirs('images', exist_ok=True)
pieces = ['pawn', 'rook', 'knight', 'bishop', 'queen', 'king']
colors = ['white', 'black']

def create_piece_image(piece, color):
    image = Image.new('RGBA', (100, 100), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    draw.text((10, 40), f"{color[0].upper()}{piece[0].upper()}", fill=(0, 0, 0), font=font)
    image.save(f'images/{color}_{piece}.png')

for color in colors:
    for piece in pieces:
        path = f'images/{color}_{piece}.png'
        if not os.path.exists(path):
            create_piece_image(piece, color)

class ChessGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Simple Chess Game")
        self.clock = pygame.time.Clock()
        self.running = True
        self.selected = None
        self.white_turn = True
        self.board = self.create_board()
        self.load_images()
        self.reset_board()

    def create_board(self):
        return [[None for _ in range(8)] for _ in range(8)]

    def load_images(self):
        self.images = {}
        for color in colors:
            for piece in pieces:
                image_path = f'images/{color}_{piece}.png'
                image = pygame.image.load(image_path).convert_alpha()
                image = pygame.transform.scale(image, (100, 100))
                self.images[f'{color}_{piece}'] = image

    def reset_board(self):
        self.board = self.create_board()
        for col in range(8):
            self.board[1][col] = 'white_pawn'
            self.board[6][col] = 'black_pawn'
        order = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook']
        for col in range(8):
            self.board[0][col] = f'white_{order[col]}'
            self.board[7][col] = f'black_{order[col]}'

    def draw_board(self):
        colors = [(240, 217, 181), (181, 136, 99)]
        for row in range(8):
            for col in range(8):
                rect = pygame.Rect(col * 100, row * 100, 100, 100)
                pygame.draw.rect(self.screen, colors[(row + col) % 2], rect)
                if self.selected == (row, col):
                    pygame.draw.rect(self.screen, (0, 255, 0), rect, 5)
                piece = self.board[row][col]
                if piece:
                    self.screen.blit(self.images[piece], (col * 100, row * 100))

    def is_valid_move(self, piece, start, end):
        sr, sc = start
        er, ec = end
        delta_r, delta_c = er - sr, ec - sc
        color, kind = piece.split("_")
        target = self.board[er][ec]

        def is_clear_path(dr, dc):
            steps = max(abs(dr), abs(dc))
            r_step = (dr // steps) if steps != 0 else 0
            c_step = (dc // steps) if steps != 0 else 0
            for step in range(1, steps):
                r = sr + r_step * step
                c = sc + c_step * step
                if self.board[r][c] is not None:
                    return False
            return True

        if target and target.startswith(color):
            return False  # can't capture own piece

        if kind == "pawn":
            direction = -1 if color == "white" else 1
            start_row = 6 if color == "black" else 1
            # move forward
            if sc == ec:
                if delta_r == direction and not target:
                    return True
                if sr == start_row and delta_r == 2 * direction and not self.board[sr + direction][sc] and not target:
                    return True
            # capture
            if abs(delta_c) == 1 and delta_r == direction and target and not target.startswith(color):
                return True
            return False

        elif kind == "rook":
            if delta_r == 0 or delta_c == 0:
                return is_clear_path(delta_r, delta_c)
            return False

        elif kind == "bishop":
            if abs(delta_r) == abs(delta_c):
                return is_clear_path(delta_r, delta_c)
            return False

        elif kind == "queen":
            if delta_r == 0 or delta_c == 0 or abs(delta_r) == abs(delta_c):
                return is_clear_path(delta_r, delta_c)
            return False

        elif kind == "king":
            return max(abs(delta_r), abs(delta_c)) == 1

        elif kind == "knight":
            return (abs(delta_r), abs(delta_c)) in [(2, 1), (1, 2)]

        return False

    def move_piece(self, start_row, start_col, end_row, end_col):
        if not (0 <= end_row < 8 and 0 <= end_col < 8):
            return
        piece = self.board[start_row][start_col]
        if not piece:
            return

        if (self.white_turn and not piece.startswith('white')) or (not self.white_turn and not piece.startswith('black')):
            return

        if self.is_valid_move(piece, (start_row, start_col), (end_row, end_col)):
            self.board[end_row][end_col] = piece
            self.board[start_row][start_col] = None
            self.white_turn = not self.white_turn

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                elif event.type == MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    row, col = y // 100, x // 100
                    if self.selected:
                        self.move_piece(*self.selected, row, col)
                        self.selected = None
                    elif self.board[row][col]:
                        self.selected = (row, col)

            self.screen.fill((0, 0, 0))
            self.draw_board()
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()

if __name__ == "__main__":
    game = ChessGame()
    game.run()
