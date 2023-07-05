import pygame
import modules.path_to_file as m_path


class Settings:
    def __init__(self, width = 0, height= 0, x= 0, y= 0, name_file = None):
        self.WIDTH = width
        self.HEIGHT = height
        self.X = x
        self.Y = y
        self.NAME_FILE = name_file
        self.IMAGE = None
        self.DIRECTION_X = False
        self.DIRECTION_Y = False
        
    def load_image(self):
        image1 = pygame.image.load(m_path.path_file(self.NAME_FILE))
        image1 = pygame.transform.scale(image1, (self.WIDTH, self.HEIGHT))
        self.IMAGE = pygame.transform.flip(image1, flip_x= self.DIRECTION_X, flip_y= self.DIRECTION_Y)

    def blit_sprite(self, screen_game):
        screen_game.blit(self.IMAGE, (self.X, self.Y))

fon = Settings(width= 1050, height= 700, x= 0, y= 0, name_file= "images/fon.jpg")
fon.load_image()
#
cells = Settings(width= 565, height= 547 ,x= 0, y = 6, name_file= "images/123.png")
cells.load_image()
#
enemy_cells  = Settings(width= 565, height= 547, x = 520, y = 6, name_file= "images/123.png")
enemy_cells.load_image()

button = Settings(width= 150, height= 50, x = 400, y = 570, name_file= "images/button1.png")
button.load_image()

ship = Settings(width= 45, height= 45, x = 100, y = 100, name_file= "images/546.png")
ship.load_image()

bot = Settings(width= 450, height= 453, x= 580, y = 73, name_file= "images/bot.png")
bot.load_image()
