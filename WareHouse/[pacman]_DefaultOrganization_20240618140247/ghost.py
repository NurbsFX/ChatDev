'''
This file contains the Ghost class.
'''
class Ghost:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        # Implement ghost movement logic here
        print("Ghost moved!")
    def __str__(self):
        return f'Ghost: x={self.x}, y={self.y}'