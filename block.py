import pygame
import modules.settings as m_set
import modules.data_base as m_data
import modules.brick as m_brick
import modules.model as m_model
pygame.init()

screen = pygame.display.set_mode((1000, 750))

class Block(m_set.Settings):
    def __init__(self, width1=0, height1=0, x1=0, y1=0):
        m_set.Settings.__init__(self, width = width1, height = height1, x = x1, y = y1)
        self.COUNT = 0
    def create_block(self, x_cor, y_cor, list_par, screen):
        x1 = x_cor
        y1 = y_cor
        for row in range(10):
            for column in range(10):
                new_brick = m_brick.Brick(
                    x_cor1 = x1, 
                    x_cor2 = x1 + 45, 
                    y_cor1 = y1, 
                    y_cor2 = y1 + 45
                    )
                new_rect = pygame.Rect(x1, y1, 35, 35)
                pygame.draw.rect(screen, (255, 0, 0), new_rect)
                list_par.append(new_brick)
                x1 += 45
            x1 = x_cor
            y1 += 45
            # print(list_par)
        
    def count(self):
        self.COUNT = 1

    def condition(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.COUNT == 1:
           new_rect = pygame.Rect(mouse_pos[0],mouse_pos[1], 35, 35)
           m_data.list_brick.append(new_rect)
           x = mouse_pos[0]
           y = mouse_pos[1]
           for new_rect in m_data.list_brick:
               self.COUNT += 1
               pygame.draw.rect(screen, (255, 0, 0), new_rect)
                
    # def blit_block(self):
    #     mouse_pos = pygame.mouse.get_pos()
    #     x = mouse_pos[0]
    #     y = mouse_pos[1]
    #     for brick in m_data.list_brick:
    #             # if self.X < x and self.X + self.WIDTH > x:
    #             #     if self.Y < y and self.Y + self.HEIGHT > y:
    #         new_rect = pygame.Rect(mouse_pos[0], mouse_pos[1], 45, 45)
    #         pygame.draw.rect(screen, (255, 0, 0), new_rect)



block = Block(35, 35, 33, 45)

enemy_block = Block(35, 35, 580, 75)
    # def create_ship(self, count_block):



    #     x1 = self.X
    #     y1 = self.Y
    #     for row in m_data.my_field:
    #         for model in row:
    #             if model == 0:
    #                 x1 = x1 + 36
    #             if model == 1:
    #                 # white_block = m_block.Block(x= x1, y= y1)
    #                 # white_block.create_block( 
    #                 #     set_column= 2,
    #                 #     set_row= 2,
    #                 #     width= 18,
    #                 #     height= 18,
    #                 #     name= "images/textures/white_brick.png"
    #                 # )
    #                 # x1 = x1 + 36
    #             if model == 2:
    #                 # tree_block = m_block.Block(x= x1, y= y1)
    #                 # tree_block.create_block( 
    #                 #     set_column= 2,
    #                 #     set_row= 2,
    #                 #     width= 18,
    #                 #     height= 18,
    #                 #     name= "images/textures/tree.png"
    #                 # )
    #                 # x1 = x1 + 36
    #             if model == 3:
    #                 # water_block = m_block.Block(x = x1, y = y1)
    #                 # water_block.create_block(
    #                 #     set_column = 2,
    #                 #     set_row = 2,
    #                 #     width = 18,
    #                 #     height = 18,
    #                 #     name = "images/textures/water_brick.png"
    #                 # )
    #                 # x1 = x1 + 36
    #         y1 = y1 + 36
    #         x1 = self.X

