import pygame
import modules.settings as m_set

pygame.init()

class Brick(m_set.Settings):
    def __init__(self, x_cor1 = 0, x_cor2 = 0, y_cor1 = 0, y_cor2 = 0):
        self.X_COR1 = x_cor1
        self.X_COR2 = x_cor2
        self.Y_COR1 = y_cor1
        self.Y_COR2 = y_cor2