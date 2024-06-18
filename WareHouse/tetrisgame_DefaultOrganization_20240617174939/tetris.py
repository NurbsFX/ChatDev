'''
This file contains the Tetris class which represents the game logic and handles the game mechanics.
'''
import pygame
from tetris import Piece
class Tetris:
    def __init__(self):
        self.width = 10
        self.height = 20
        self.grid = [[0] * self.width for _ in range(self.height)]
        self.current_piece = None
        self.next_piece = None
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
        self.game_over = False
    def run(self):
        # Initialize the game window
        pygame.display.set_caption("Tetris")
        self.screen = pygame.display.set_mode((self.width * 30, self.height * 30))
        clock = pygame.time.Clock()
        while not self.game_over:
            self.handle_events()
            self.update()
            self.draw()
            clock.tick(10 * self.level)
        pygame.quit()
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.move_piece(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    self.move_piece(1, 0)
                elif event.key == pygame.K_DOWN:
                    self.move_piece(0, 1)
                elif event.key == pygame.K_UP:
                    self.rotate_piece()
    def update(self):
        # Update the game state
        if self.current_piece is None:
            self.spawn_piece()
        if not self.check_collision(0, 1):
            self.move_piece(0, 1)
        else:
            self.lock_piece()
            self.clear_lines()
            self.spawn_piece()
    def draw(self):
        # Draw the game screen
        self.screen.fill((0, 0, 0))
        self.draw_grid()
        self.draw_piece()
        pygame.display.flip()
    def move_piece(self, dx, dy):
        # Move the current piece
        if self.current_piece is not None:
            new_x = self.current_piece.x + dx
            new_y = self.current_piece.y + dy
            if not self.check_collision(dx, dy):
                self.current_piece.x = new_x
                self.current_piece.y = new_y
    def rotate_piece(self):
        # Rotate the current piece
        if self.current_piece is not None:
            rotated_piece = self.current_piece.rotate()
            if not self.check_collision(0, 0, rotated_piece):
                self.current_piece = rotated_piece
    def spawn_piece(self):
        # Spawn a new piece
        self.current_piece = self.next_piece
        self.next_piece = Piece()
        if self.check_collision(0, 0):
            self.game_over = True
    def lock_piece(self):
        # Lock the current piece in the grid
        for y in range(self.current_piece.size):
            for x in range(self.current_piece.size):
                if self.current_piece.shape[y][x] != 0:
                    self.grid[self.current_piece.y + y][self.current_piece.x + x] = self.current_piece.color
    def clear_lines(self):
        # Clear completed lines
        lines_cleared = 0
        new_grid = []
        for y in range(self.height):
            if not all(self.grid[y]):
                new_grid.append(self.grid[y])
            else:
                lines_cleared += 1
        new_grid = [[0] * self.width for _ in range(lines_cleared)] + new_grid
        self.grid = new_grid
        self.lines_cleared += lines_cleared
        self.score += lines_cleared * lines_cleared * 100
        self.level = self.lines_cleared // 10 + 1
    def check_collision(self, dx, dy, piece=None):
        # Check if there is a collision with the grid or another piece
        if piece is None:
            piece = self.current_piece
        for y in range(piece.size):
            for x in range(piece.size):
                if piece.shape[y][x] != 0:
                    new_x = piece.x + x + dx
                    new_y = piece.y + y + dy
                    if new_x < 0 or new_x >= self.width or new_y >= self.height or self.grid[new_y][new_x] != 0:
                        return True
        return False
    def draw_grid(self):
        # Draw the grid
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(self.screen, (128, 128, 128), (x * 30, y * 30, 30, 30), 1)
                if self.grid[y][x] != 0:
                    pygame.draw.rect(self.screen, self.grid[y][x], (x * 30 + 1, y * 30 + 1, 28, 28))
    def draw_piece(self):
        # Draw the current piece
        if self.current_piece is not None:
            for y in range(self.current_piece.size):
                for x in range(self.current_piece.size):
                    if self.current_piece.shape[y][x] != 0:
                        pygame.draw.rect(self.screen, self.current_piece.color,
                                         ((self.current_piece.x + x) * 30 + 1, (self.current_piece.y + y) * 30 + 1, 28, 28))
class Piece:
    def __init__(self):
        self.x = 4
        self.y = 0
        self.size = 4
        self.shape = [
            [0, 0, 0, 0],
            [1, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.color = (255, 0, 0)
    def rotate(self):
        # Rotate the piece
        rotated_piece = Piece()
        rotated_piece.x = self.x
        rotated_piece.y = self.y
        rotated_piece.size = self.size
        rotated_piece.shape = [[0] * self.size for _ in range(self.size)]
        for y in range(self.size):
            for x in range(self.size):
                rotated_piece.shape[y][x] = self.shape[self.size - x - 1][y]
        return rotated_piece