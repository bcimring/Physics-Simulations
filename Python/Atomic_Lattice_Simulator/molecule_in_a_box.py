#####################################################
# This is a solid state physics simulation of atoms #
# in a box, displaying aspects of kinetic/ss theory #
# in monatomic molecules                            #
#####################################################

import pygame
from random import randint
from Molecule.molecule import Molecule
from Molecule.lattice import Lattice
from math import ceil
from math import sqrt

dt = 0.0001
N = int(input("Input number molecules: "))
m_max = int(input("Input max mass: "))
v_max = 0
WIDTH = 500
HEIGHT = 500

grid_size = ceil(sqrt(N))

lat = Lattice( grid_size, m_max, 10, WIDTH, HEIGHT, v_max )

lat.mol_list[12].y_to_ev -= 32.99
lat.mol_list[12].y_l -= 33.01
lat.mol_list[12].x_to_ev -= 32.99
lat.mol_list[12].x_l -= 33.01

w = grid_size
h = grid_size
k = 10000
gamma = 0

pygame.init()
game_window = pygame.display.set_mode((WIDTH,HEIGHT))

exit_flag= False
play_flag = True

# calc_avg_speed( lat.mol_list )

while not exit_flag:
    # restart animation if stopped
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        play_flag = True

    # close animation
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_flag = True
    
    while play_flag:
        # stop game
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            play_flag = False
            
        # close animation
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_flag = True
                play_flag = False

        #check_collisions( mol_list, dt )
        lat.evolve( dt, w, h, k, gamma , WIDTH, HEIGHT)
        lat.draw_screen(game_window)
        lat.update_positions()
        lat.follow_cm( WIDTH, HEIGHT )

pygame.quit()


# calc_avg_speed( lat.mol_list )
