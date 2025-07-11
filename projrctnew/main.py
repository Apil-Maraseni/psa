# SAME IMPORTS
import pygame
from pygame.locals import *
from PIL import Image, ImageDraw, ImageFont
import os
import sys

# PIECE SETUP
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
        pygame.display.set_caption("Chess with Check/Checkmate")
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
            self.board[1][col] = 'black_pawn'
            self.board[6][col] = 'white_pawn'
        order = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook']
        for col in range(8):
            self.board[0][col] = f'black_{order[col]}'
            self.board[7][col] = f'white_{order[col]}'

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

        # Highlight possible moves
        if self.selected:
            piece = self.board[self.selected[0]][self.selected[1]]
            for r in range(8):
                for c in range(8):
                    if self.is_valid_move(piece, self.selected, (r, c)):
                        pygame.draw.circle(self.screen, (0, 255, 0), (c * 100 + 50, r * 100 + 50), 10)

    def draw_turn_indicator(self):
        color = (255, 255, 255) if self.white_turn else (0, 0, 0)
        pygame.draw.rect(self.screen, color, pygame.Rect(700, 0, 100, 20))

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
            return False

        if kind == "pawn":
            direction = -1 if color == "white" else 1
            start_row = 6 if color == "white" else 1
            if sc == ec:
                if delta_r == direction and not target:
                    return True
                if sr == start_row and delta_r == 2 * direction and not self.board[sr + direction][sc] and not target:
                    return True
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

    # ----------- Check and Checkmate Logic -------------
    def find_king(self, color):
        for r in range(8):
            for c in range(8):
                if self.board[r][c] == f"{color}_king":
                    return (r, c)
        return None

    def is_square_attacked(self, row, col, by_color):
        for r in range(8):
            for c in range(8):
                attacker = self.board[r][c]
                if attacker and attacker.startswith(by_color):
                    if self.is_valid_move(attacker, (r, c), (row, col)):
                        return True
        return False

    def is_in_check(self, color):
        king_pos = self.find_king(color)
        if king_pos:
            return self.is_square_attacked(*king_pos, 'black' if color == 'white' else 'white')
        return False

    def has_legal_moves(self, color):
        for r1 in range(8):
            for c1 in range(8):
                piece = self.board[r1][c1]
                if piece and piece.startswith(color):
                    for r2 in range(8):
                        for c2 in range(8):
                            if self.is_valid_move(piece, (r1, c1), (r2, c2)):
                                backup = self.board[r2][c2]
                                self.board[r2][c2] = piece
                                self.board[r1][c1] = None
                                in_check = self.is_in_check(color)
                                self.board[r1][c1] = piece
                                self.board[r2][c2] = backup
                                if not in_check:
                                    return True
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
            backup = self.board[end_row][end_col]
            self.board[end_row][end_col] = piece
            self.board[start_row][start_col] = None

            color = 'white' if piece.startswith('white') else 'black'
            if self.is_in_check(color):
                self.board[start_row][start_col] = piece
                self.board[end_row][end_col] = backup
                return

            self.white_turn = not self.white_turn

            enemy = 'white' if not self.white_turn else 'black'
            if self.is_in_check(enemy):
                print(f"{enemy.capitalize()} is in CHECK!")
                if not self.has_legal_moves(enemy):
                    print(f"CHECKMATE! {'White' if piece.startswith('white') else 'Black'} wins!")
                    self.running = False

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
                        if (self.white_turn and self.board[row][col].startswith("white")) or \
                           (not self.white_turn and self.board[row][col].startswith("black")):
                            self.selected = (row, col)
                        else:
                            self.selected = None
                    else:
                        self.selected = None

            self.screen.fill((0, 0, 0))
            self.draw_board()
            self.draw_turn_indicator()
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = ChessGame()
    game.run()
