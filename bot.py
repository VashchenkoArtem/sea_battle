import pygame

pygame.init()

def check_pos(mouse_pos, mouse_x, mouse_y):
    if mouse_pos[0] > 580 and mouse_pos[0] < 625:
        mouse_x = 0
        print("1x")
    if 670 > mouse_pos[0] > 625 :
        mouse_x = 1
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
    