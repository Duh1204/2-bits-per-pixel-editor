import pygame
from constants import *
from drawgrid import Grid

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('2BPP')
window.fill(COLOR0)
mouse_press = False


def run():
    global mouse_press
    game = True
    clock = pygame.time.Clock()
    grid = Grid(window)
    while game:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_press = True
            if event.type == pygame.MOUSEMOTION and mouse_press:
                pos = pygame.mouse.get_pos()
                x_col = pos[0]
                y_row = pos[1]
                grid.draw_with_mouse(x_col // TILESIZE, y_row // TILESIZE)
            if event.type == pygame.MOUSEBUTTONUP:
                grid.reset_pressed_color()
                mouse_press = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    grid.to_hex()
                elif event.key == pygame.K_x:
                    grid.from_hex()

        pygame.display.update()
    pygame.quit()


run()
