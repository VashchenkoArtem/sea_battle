import pygame
import modules.path_to_file as m_path

pygame.init()

class Ships:
    def __init__(self, width, height, x, y, name_file):
        self.WIDTH = width
        self.HEIGHT = height
        self.X = x
        self.Y = y
        self.NAME_FILE = name_file
        self.IMAGE = None
        self.X_DIRECION = False
        self.Y_DIRECTION = False

    def load_image(self):
        image = pygame.image.load(m_path.path_file(self.NAME_FILE))
        image = pygame.transform.scale(image, (self.WIDTH, self.HEIGHT))

    def blit_sprite(self, screen_game):
        screen_game.blit(self.IMAGE, (self.X, self.Y))

