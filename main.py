import pygame
import sys
import modules.settings as m_set
import modules.data_base as m_data
import modules.create_field as m_field
import modules.block as m_block
import random 
import modules.bot as m_bot
ship1 = m_set.Settings()
bb = 0
choose = 0
bot_explosion1 = 0
bot_explosion2 = 0
bot_explosion3 = 0
bot_explosion4 = 0
bot_explosion5 = 0
bot_explosion6 = 0
bot_explosion7 = 0
bot_explosion8 = 0
bot_explosion9 = 0
bot_explosion10 = 0
enemy_ships = 10

got = 0
a6 = 0
a7 = 0
a8 = 0
a5 = 0
a4 = 0
a2 = 0
a3 = 0
a1 = 0
cou = 1
sps = 0
u = 0
vot = 0
ship_size = 4
pygame.init()
count_field = 0
enemy_field = [[0] * 10 for _ in range(10)]
def func(x, y):
    global got

    if got == 1:
        print("asdasdas")
        x1 = x * 45
        y1 = y * 45
        ship1 = m_set.Settings(45, 45, x1, y1, name_file= 'images/ship.png')
        ship1.load_image()
        ship1.blit_sprite()

def place_ships():
    board = [[0] * 10 for _ in range(10)]#создає поле
    ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1] 

def examination(x, y, ship_size, enemy_field):
    for i in range(ship_size):
                # перевіряємо правильно розміщен корабель чи ні
        if y + i >= 10 or enemy_field[x][y + i] == 1:
            return False
        if x > 0 and enemy_field[x - 1][y + i] == 1:
            return False
        if x < 9 and enemy_field[x + 1][y + i] == 1:
            return False
        if y > 0 and enemy_field[x][y + i - 1] == 1:
            return False
        if y + i < 9 and enemy_field[x][y + i + 1] == 1:
            return False 
    return True
    
def check_hit(row, col, enemy_board):
    if enemy_board[row][col] == "S":
        return True
    else:
        return False
    # for ship_size in ships:
    #     while True:
    #         x = random.randint(0, 9)
    #         y = random.randint(0, 9)
    #         direction = random.choice(['horizontal', 'vertical'])
            
    #         if examination(x, y, ship_size, direction):
    #             if direction == 'horizontal':
    #                 for i in range(ship_size):
    #                     enemy_field[x][y + i] = 1# звертаємось до певної комірки та ставимо 1 для того, щоб розуміти що у цій комірці щось стоїть
    #             else:
    #                 for i in range(ship_size):
    #                     enemy_field[x + i][y] = 1# звертаємось до певної комірки та ставимо 1 для того, щоб розуміти що у цій комірці щось стоїть
    #             break
                    
    # return board
# font = pygame.font.SysFont()
def check(x, y):
    global got
    if mouse_x == x and mouse_y == y:
        got = 1
def draw_board(board):
    count = 0
    for x in range(10):
        for y in range(10):
            if board[x][y] == 1:
                if count == 0: 
                    for i in range(4):
                        rect = pygame.Rect((x * 45 + 580, y * 45 + 75), (45, 45))
                        pygame.draw.rect(screen, (0, 0, 0), rect)
                        # m_set.bot.blit_sprite(screen_game=screen)

field_size = 10
cell_size = 45
field_x = (1050 - field_size * cell_size) // 2 - 240
field_y = (700 - field_size * cell_size) // 2 - 50
enemy_field_x = (1050 - field_size * cell_size) // 2 - 20
enemy_field_y = (700 - field_size * cell_size) // 2 - 50


# Создание поля
field = []
for i in range(field_size):
    row = []
    for j in range(field_size):
        row.append(0)
    field.append(row)

# Функция для проверки возможности размещения корабля
def is_valid_placement(row, col, length, direction):
    if direction == 'horizontal':
        for j in range(col, col + length):
            if field[row][j] == 1 or (row > 0 and field[row - 1][j] == 1) or (row < field_size - 1 and field[row + 1][j] == 1):
                return False
    elif direction == 'vertical':
        for i in range(row, row + length):
            if field[i][col] == 1 or (col > 0 and field[i][col - 1] == 1) or (col < field_size - 1 and field[i][col + 1] == 1):
                return False
    return True

io = 0
bot = 0         
spd = 0
x = random.randint(0, 9)
y = random.randint(0, 9)
x1 = random.randint(0, 9)
x1_1 = x1 + 45
y1 = random.randint(0, 9)
y1_1 = y1 + 45
x2 = random.randint(0, 9)
y2 = random.randint(0, 9)
x3 = random.randint(0, 9)
y3 = random.randint(0, 9)
x4 = random.randint(0, 9)
y4 = random.randint(0, 9)
x5 = random.randint(0, 9)
y5 = random.randint(0, 9)
x6 = random.randint(0, 9)
y6 = random.randint(0, 9)
x7 = random.randint(0, 9)
y7 = random.randint(0, 9)
x8 = random.randint(0, 9)
y8 = random.randint(0, 9)
x9 = random.randint(0, 9)
y9 = random.randint(0, 9)
enemy_count_cell = 1
count_cell = 0
count_button = 0
count = 0
enemy_draw = 0
screen = pygame.display.set_mode((1050, 700))
# 400, 570
# my_board = my_place_ship()
board = place_ships()
fon_button = pygame.Rect(400, 570, 150, 100)
x = random.randint(580, 1030)
y = random.randint(75, 520)
dew = 0
font = pygame.font.SysFont('italic', size= 50, bold= True)
m_block.block.create_block(58, 72, m_data.my_field, screen)
m_block.enemy_block.create_block(580, 75, m_data.enemy_field, screen)
game = True
draw = 0
while game:

    m_set.fon.blit_sprite(screen_game=screen)
    m_set.button.blit_sprite(screen_game= screen)
    
    # m_set.ship.blit_sprite(screen_game= screen)
    m_set.cells.blit_sprite(screen_game= screen)
    m_set.enemy_cells.blit_sprite(screen_game= screen)
    m_block.block.condition()
    # draw_field()
    # if io == 1:
    #     screen.blit(screen)
    if bb == 1:
        rect = pygame.rect.Rect((random_x , random_y), (45, 45))
        pygame.draw.rect(screen, (255, 255, 255), rect)
    func(x, y)
    if sps == 1:
        rect = pygame.Rect((x * 45 + 580, y * 45 + 75), (45, 45))
        pygame.draw.rect(screen,(255, 0, 0), rect)
        rect = pygame.Rect((x * 45 + 580 + 45, y * 45 + 75), (45, 45))
        pygame.draw.rect(screen, (255, 0, 0), rect)
        rect = pygame.Rect((x * 45 + 580 + 90, y * 45 + 75), (45, 45))
        pygame.draw.rect(screen,(255, 0, 0), rect)
        rect = pygame.Rect((x * 45 + 580+ 135, y * 45 + 75), (45, 45))
        pygame.draw.rect(screen,(255, 0, 0), rect)
        # cou = 2

    if spd == 1:

        rect = pygame.Rect((x1 * 45 + 580, y1 * 45 + 75), (45, 45))
        pygame.draw.rect(screen,(255, 0, 0), rect)
        rect = pygame.Rect((x1 * 45 + 580+ 45, y1 * 45 + 75), (45, 45))
        pygame.draw.rect(screen,(255, 0, 0), rect)
        rect = pygame.Rect((x1 * 45 + 580+ 90, y1 * 45 + 75), (45, 45))
        pygame.draw.rect(screen,(255, 0, 0), rect)
    
    if a1 == 1:
        rect = pygame.Rect((x2 * 45 + 580, y2 * 45 + 75), (45, 45))
        pygame.draw.rect(screen,(255, 0, 0), rect)
        rect = pygame.Rect((x2 * 45 + 580+ 45, y2 * 45 + 75), (45, 45))
        pygame.draw.rect(screen,(255, 0, 0), rect)
        rect = pygame.Rect((x2 * 45 + 580+ 90, y2 * 45 + 75), (45, 45))
        pygame.draw.rect(screen,(255, 0, 0), rect)
        # print("sddsd")
    if a2 == 1:
        rect = pygame.Rect((x3 * 45 + 580, y3 * 45 + 75), (45, 45))
        pygame.draw.rect(screen,(255, 0, 0), rect)
        rect = pygame.Rect((x3 * 45 + 580+ 45, y3 * 45 + 75), (45, 45))
        pygame.draw.rect(screen,(255, 0, 0), rect)

    if a3 == 1:
        rect = pygame.Rect((x4 * 45 + 580, y4 * 45 + 75), (45, 45))
        pygame.draw.rect(screen,(255, 0, 0), rect)
        rect = pygame.Rect((x4 * 45 + 580+ 45, y4 * 45 + 75), (45, 45))
        pygame.draw.rect(screen,(255, 0, 0), rect)
    if a4 == 1:
        rect = pygame.Rect((x5 * 45 + 580, y5 * 45 + 75), (45, 45))
        pygame.draw.rect(screen,(255, 0, 0), rect)
        rect = pygame.Rect((x5 * 45 + 580+ 45, y5 * 45 + 75), (45, 45))
        pygame.draw.rect(screen,(255, 0, 0), rect)
    
    if a5 == 1:
        rect = pygame.Rect((x6 * 45 + 580, y6 * 45 + 75), (45, 45))
        pygame.draw.rect(screen,(255, 0, 0), rect)
    if a6 == 1:
        rect = pygame.Rect((x7 * 45 + 580, y7 * 45 + 75), (45, 45))
        pygame.draw.rect(screen,(255, 0, 0), rect)  
    if a7 == 1:
        rect = pygame.Rect((x8 * 45 + 580, y8 * 45 + 75), (45, 45))
        pygame.draw.rect(screen,(255, 0, 0), rect) 
    if a8 == 1:
        rect = pygame.Rect((x9 * 45 + 580, y9 * 45 + 75), (45, 45))
        pygame.draw.rect(screen,(255, 0, 0), rect) 
    
    if pygame.mouse.get_pressed()[0]:  # Левая кнопка мыши
        # mouse_x, mouse_y = pygame.mouse.get_pos()
       
       if field_x <= mouse_x < field_x + field_size * cell_size and field_y <= mouse_y < field_y + field_size * cell_size:
            col = (mouse_x - field_x) // cell_size
            row = (mouse_y - field_y) // cell_size

            if field[row][col] == 0 and is_valid_placement(row, col, 1, 'horizontal'):
                field[row][col] = 1
    # if bot == 1:
    #     draw_board(board= board)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            
            mouse_pos = pygame.mouse.get_pos()
            mouse_y = mouse_pos[0]
            mouse_x = mouse_pos[1]
            check(x, y)
            check(x1, y1)
            check(x2, y2)
            check(x3, y3)
            check(x4, y4)
            check(x5, y5)
            check(x6, y6)
            check(x7, y7)
            check(x8, y8)
            check(x9, y9)
            if mouse_pos[0] > 580 and mouse_pos[0] < 625:
                mouse_x = 0
            if 670 > mouse_pos[0] > 625 :
                mouse_x= 1
            if mouse_pos[0] > 670:
                mouse_x = 2
            if mouse_pos[0] > 715:
                mouse_x = 3
            if mouse_pos[0] > 760:
                mouse_x = 4
            if mouse_pos[0] > 805:
                mouse_x = 5
            if mouse_pos[0] > 850:
                mouse_x = 6
            if mouse_pos[0] > 895:
                mouse_x = 7
            if mouse_pos[0] > 940:
                mouse_x = 8
            if mouse_pos[0] > 985:
                mouse_x = 9
            if mouse_pos[1] > 75:
                mouse_y = 0
            if mouse_pos[1] > 120:
                mouse_y = 1
            if mouse_pos[1] > 165:
                mouse_y = 2
            if mouse_pos[1] > 210:
                mouse_y = 3
            if mouse_pos[1] > 255:
                mouse_y = 4
            if mouse_pos[1] > 300:
                mouse_y = 5
            if mouse_pos[1] > 345:
                mouse_y = 6
            if mouse_pos[1] > 390:
                mouse_y = 7
            if mouse_pos[1] > 435:
                mouse_y = 8
            if mouse_pos[1] > 480:
                mouse_y = 9 
               # print("asdasd")
            count_cell += 1
            clicked_cell = (mouse_pos[0] // 45, mouse_pos[1] // 45)
            if 575 > mouse_pos[0] > 380 and 630 > mouse_pos[1] > 550:
                bot = 1
                if 0 <= clicked_cell[0] < 10 and 0 <= clicked_cell[1] < 10:  # Перевірка допустимих індексів
                    if board[clicked_cell[0]][clicked_cell[1]] == 1:# Перевірка чи стоїть щось у певній комірці
                        board[clicked_cell[0]][clicked_cell[1]] = 2

                        print("sodksaosa")       
            for cell in m_data.my_field:
                if  cell.X_COR1 < mouse_pos[0] and cell.X_COR2 > mouse_pos[0]:
                    if cell.Y_COR1 < mouse_pos[1] and cell.Y_COR2 > mouse_pos[1]:
                        if count_cell == 1 :
                            # m_bot.draw_board(my_board)
                            for i in range(4):
                                new_rect = pygame.Rect(cell.X_COR1, cell.Y_COR1, 45, 45)
                                cell.X_COR1 += 45
                                m_data.list_ship.append(new_rect)
                                draw = 1
                        if count_cell == 2 or count_cell == 3:
                            for i in range(3):
                                new_rect1 = pygame.Rect(cell.X_COR1, cell.Y_COR1, 45, 45)
                                cell.X_COR1 += 45
                                m_data.list_ship1.append(new_rect1)
                         
                                dew = 1
                            cell.X_COR1 = cell.X_COR1 - 45 
                            print(count_cell)
                        elif count_cell == 4 or count_cell == 5 or count_cell == 6:
                                for i in range(2):
                                    new_rect = pygame.Rect(cell.X_COR1, cell.Y_COR1, 45, 45)
                                    cell.X_COR1 += 45
                                    m_data.list_ship.append(new_rect)
                                    draw = 1
                                # count_cell += 1
                        elif count_cell == 7 or count_cell == 8 or count_cell == 9 or count_cell == 10:
                            new_rect = pygame.Rect(cell.X_COR1, cell.Y_COR1, 45, 45)
                            cell.X_COR1 += 45
                            m_data.list_ship.append(new_rect)
                            draw = 1
            if 585 > mouse_pos[0] > 375 and 625 > mouse_pos[1] > 560:
                    for enemy_cell in m_data.enemy_field:

                        if enemy_cell.X_COR1 < x and enemy_cell.X_COR2 > x:    
                            if enemy_cell.Y_COR1 < y and enemy_cell.Y_COR2 > y:
                                    
                                    examination(x1, y1, 3, enemy_field)
                                    examination(x2, y2, 3, enemy_field)
                                    examination(x3, y3, 2, enemy_field)
                                    examination(x4, y4, 2, enemy_field)
                                    examination(x5, y5, 2, enemy_field)
                                    examination(x6, y6, 1, enemy_field)
                                    examination(x7, y7, 1, enemy_field)
                                    examination(x8, y8, 1, enemy_field)
                                    examination(x9, y9, 1, enemy_field)
                                    # func(x, y, 1,)
                                    x = random.randint(0, 9)
                                    y = random.randint(0, 9)
                                    if vot == 0:
                                        examination(x, y, 4, enemy_field)
                                        print(x, y)
                                        
                                        for i in range(4):

                                            number = 4
                                            enemy_field[x][y] = 1
                                            x += 45                                      
                                            x = x - 45

                                            vot = 1
                                                # if enemy_field[x][y] == 1 and enemy_field[x + 1][y] == 0 and enemy_field[x - 1][y] == 0 and enemy_field[x][y - 1] == 0 and enemy_field[x][y + 1] == 0 and enemy_field[x + 1][y + 1] == 0 and enemy_field[x - 1][y + 1] == 0 and enemy_field[x + 1][ y- 1] == 0 and enemy_field[x - 1][ y - 1] == 0 and x + ship_size < 9 and x > 0 and y + ship_size < 9 and y > 0:
                                            sps = 1
                                            ship_size = ship_size - 1


                                        if vot == 1:
                                                
                                            enemy_field[x1][y1] = 1
                                            for i in range(3):
                                                number = 3
                                                x += 45
                                                x = x - 45
                                                spd = 1
                                                vot = 2



                                        if vot == 2:
                                                
                                            enemy_field[x2][y2] = 1
                                            for i in range(3):
                                                number = 3
                                                x += 45
                                                x = x - 45
                                                spd = 1
                                                vot = 3
                                                a1 = 1
                                                a1_1 = a2 + 45


                                        if vot == 3:
                                            
                                            for i in range(3):
                                                enemy_field[x3][y3] = 1
                                                number = 3
                                                x += 45
                                                x = x - 45
                                                vot = 4
                                                a2 = 1
                                                a2_1 = a1 + 45
                                        if vot == 4:
                                            
                                            for i in range(2):
                                                enemy_field[x4][y4] = 1    
                                                number = 2
                                                x += 45
                                                x = x - 45
                                                vot = 5
                                                a3 = 1
                                        x5 = random.randint(0, 9)
                                        y5 = random.randint(0, 9)
                                        if vot == 5:
                                           
                                            for i in range(2):
                                                enemy_field[x5][y5] = 1
                                                number = 2
                                                x += 45
                                                x = x - 45
                                                vot = 6
                                                a4 = 1
                                        x6 = random.randint(0, 9)
                                        y6 = random.randint(0, 9)
                                        if vot == 6:
                                            enemy_field[x6 ][y6] = 1
                                            number = 1
                                            x += 45
                                            x = x - 45
                                            vot = 7
                                            a5 = 1    

                                        x7 = random.randint(0, 9)
                                        y7 = random.randint(0, 9)
                                        if vot == 7:
                                            enemy_field[x7][y7] = 1
                                            number = 1
                                            x += 45
                                            x = x - 45
                                            vot = 8
                                            a6 = 1
                                        x8 = random.randint(0, 9)
                                        y8 = random.randint(0, 9)
                                        if vot == 8:
                                            enemy_field[x8][y8] = 1
                                            number = 1
                                            vot = 9
                                            a7 = 1
                                        x9 = random.randint(0, 9)
                                        y9 = random.randint(0, 9)
                                        if vot == 9:
                                            enemy_field[x9][y9]
                                            number = 1
                                            vot = 9
                                            a8 = 1

                                    print(x1, y1)
                                    # x_1 = x * 45
        
            
            if 580  < mouse_pos[0] < 1025 and mouse_pos[1] < 520 and choose == 0:
                print("Твій ход")
                if mouse_x == x and mouse_y == y:
                    print("Ви влучили!")
                    bot_explosion1 = 1
                if mouse_x == x1 and mouse_y == y1: 
                    print("Ви влучили!")
                    bot_explosion2 = 1
                if mouse_x == x2 and mouse_y == y2:
                    print("Ви влучили!")
                    bot_explosion3 = 1
                if mouse_x == x3 and mouse_y == y3:
                    print("Ви влучили!")
                    bot_explosion4 = 1
                if mouse_x == x4 and mouse_y == y4:
                    print("Ви влучили!")
                    bot_explosion5 = 1
                if mouse_x == x5 and mouse_y == y5:
                    print("Ви влучили!")
                    bot_explosion6 = 1
                if mouse_x == x6 and mouse_y == y6:
                    print("Ви влучили!")
                    bot_explosion7 = 1
                if mouse_x == x7 and mouse_y == y7:
                    print("Ви влучили!")
                    bot_explosion8 = 1     
                if mouse_x == x8 and mouse_y == y8:
                    print("Ви влучили!")
                    bot_explosion9 = 1             
                if mouse_x == x9 and mouse_y == y9:
                    print("Ви влучили!") 
                    bot_explosion10 = 1
                choose = 1
            if choose == 1:
                random_x = random.randint(60, 465)
                random_y = random.randint(75, 475)
                bb = 1
                print("Ход противника")
                choose = 0
                if cell.X_COR1 < random_x < cell.X_COR2 and cell.Y_COR1 < random_y < cell.Y_COR2:

                    print("Противник влучив")
                print(choose)
               # x_2 = x_1 + 45
            # if mouse_x == x:
            #     print("asdasdadasdad")
        

                # print("sadasd")
                # if y1 * 45 > mouse_pos[1] and mouse_pos[1]:
                #     ship1 = m_set.Settings(45, 45, x1, y1, "images/ship.png")
                #     ship1.load_image()
                #     print(x, y)
                #     ship1.blit_sprite(screen_game= screen)
                #     print('adsf')                      
            print(mouse_pos)    
    if enemy_draw == 1:
        for enemy_ship in m_data.enemy_list_ship:
            pygame.draw.rect(screen, (255, 0, 0), enemy_ship)
    if dew == 1:
        for ship in m_data.list_ship1:
            pygame.draw.rect(screen, (255, 0, 0), ship)
    if draw == 1:
        for ship in m_data.list_ship:
            pygame.draw.rect(screen, (255, 0, 0), ship)    
    m_set.bot.blit_sprite(screen_game= screen)
    if bot_explosion1 == 1:
        ship1 = m_set.Settings(45, 45, x * 45 + 580, y * 45 + 75, "images/Explosion.png")
        ship1.load_image()
        ship1.blit_sprite(screen)
    if bot_explosion2 == 1:
        ship1 = m_set.Settings(45, 45, x1 * 45 + 580, y1 * 45 + 75, "images/Explosion.png")
        ship1.load_image()
        ship1.blit_sprite(screen)
    if bot_explosion3 == 1:
        ship1 = m_set.Settings(45, 45, x2 * 45 + 580, y2 * 45 + 75, "images/Explosion.png")
        ship1.load_image()
        ship1.blit_sprite(screen)
    if bot_explosion4 == 1:
        ship1 = m_set.Settings(45, 45, x3 * 45 + 580, y3 * 45 + 75, "images/Explosion.png")
        ship1.load_image()
        ship1.blit_sprite(screen)
    if bot_explosion5 == 1:
        ship1 = m_set.Settings(45, 45, x4 * 45 + 580, y4 * 45 + 75, "images/Explosion.png")
        ship1.load_image()
        ship1.blit_sprite(screen)
    if bot_explosion6 == 1:
        ship1 = m_set.Settings(45, 45, x5 * 45 + 580, y5 * 45 + 75, "images/Explosion.png")
        ship1.load_image()
        ship1.blit_sprite(screen)
    if bot_explosion7 == 1:
        ship1 = m_set.Settings(45, 45, x6 * 45 + 580, y6 * 45 + 75, "images/Explosion.png")
        ship1.load_image()
        ship1.blit_sprite(screen)
    if bot_explosion8 == 1:
        ship1 = m_set.Settings(45, 45, x7 * 45 + 580, y7 * 45 + 75, "images/Explosion.png")
        ship1.load_image()
        ship1.blit_sprite(screen)
    if bot_explosion9 == 1:
        ship1 = m_set.Settings(45, 45, x8 * 45 + 580, y8 * 45 + 75, "images/Explosion.png")
        ship1.load_image()
        ship1.blit_sprite(screen)
    if bot_explosion10 == 1:
        ship1 = m_set.Settings(45, 45, x9 * 45 + 580, y9 * 45 + 75, "images/Explosion.png")
        ship1.load_image()
        ship1.blit_sprite(screen)
    pygame.display.flip()

