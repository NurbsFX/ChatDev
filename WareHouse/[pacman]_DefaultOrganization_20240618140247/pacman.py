'''
This file contains the Pacman class.
'''
class Pacman:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, direction):
        if direction == 'up':
            self.y -= 1
        elif direction == 'down':
            self.y += 1
        elif direction == 'left':
            self.x -= 1
        elif direction == 'right':
            self.x += 1
    def eat_dot(self):
        # Implement dot eating logic here
        print("Pacman ate a dot!")
    def eat_ghost(self):
        # Implement ghost eating logic here
        print("Pacman ate a ghost!")
    def __str__(self):
        return f'Pacman: x={self.x}, y={self.y}'