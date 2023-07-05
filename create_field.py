# import pygame
# import modules.settings as m_set
# import modules.data_base as m_data
# import modules.block as m_block

# pygame.init()

# class Field(m_set.Settings):
#     def __init__(self, x, y):
#         m_set.Settings.__init__(self, x= x, y= y)
    
#     def create_field(self):
#         x1 = self.X
#         y1 = self.y
#         for row in m_data.my_field:
#             for model in row:
#                 if model == 0:
#                     x1=x1 + 30
#                     if model == 1:
#                         ship = m_block.Block(x = x1, y1 = y1)
#                         ship.create_block(width = 30,
#                                           height= 30,
#                                           name= "images/ship.png")
#                         x1 = x1 + 30
#                     y1 = y1 + 30
#                     x1 = self.X
                    
# field = Field(x = 0, y = 0)
# field.create_field
# print(len(m_data.list_block))
