from math import acos
from math import cos
from math import sin
from math import sqrt
from math import pi
from random import randint
import pygame
from Molecule.molecule import Molecule

class Lattice(object):

    def __init__(self, grid_size, mass, radius, width, height, v_max ):
        self.mol_list = []

        grid_length = width/grid_size

        # intitialize molecule list
        for j in range(grid_size):
            for i in range(grid_size):
                mol = Molecule( 10 , ((i + 1/2)*grid_length), ((j + 1/2)*grid_length), randint(-v_max, v_max), randint(-v_max, v_max), (255, 255, 255 ), mass, i)
                self.mol_list.append(mol)
    
    def update_positions( self ):
        for mol in self.mol_list:
            mol.x_to_ev = mol.x
            mol.y_to_ev = mol.y

    def follow_cm(self, WIDTH, HEIGHT ):
        x_cm = 0
        y_cm = 0
        M = 0

        for mol in self.mol_list:
            x_cm += mol.x_to_ev*mol.m
            y_cm += mol.y_to_ev*mol.m
            M += mol.m
        x_cm /= M
        y_cm /= M

        x_cm -= WIDTH/2
        y_cm -= HEIGHT/2


        for mol in self.mol_list:
            mol.x_to_ev -= x_cm
            mol.y_to_ev -= y_cm
            mol.x -= x_cm
            mol.y -= y_cm
            mol.x_l -= x_cm
            mol.y_l -= y_cm

    def apply_collisions( self, dt ):

        # check if collide with other molecule
        for i in range(1,len(self.mol_list)):
            for j in range(i):
                if self.mol_list[i].check_collision(self.mol_list[j]):
                    self.mol_list[i].collide_with(self.mol_list[j], dt)

        # check if collide with wall
        for mol in self.mol_list:
            x = False
            y = False
            if ( ((mol.x-mol.radius) < 0) or ((mol.x+mol.radius) > WIDTH)) :
                x = True
            if ( ((mol.y-mol.radius) < 0) or ((mol.y+mol.radius) > HEIGHT)):
                y = True

            mol.keep_on_screen( x, y )
            
        return 

    def evolve( self, dt, n_columns, n_rows, k, gamma, WIDTH, HEIGHT ):
        for i in range(n_rows):
            for j in range(n_columns):
                idx = i*n_columns + j
                
                top, bottom, left, right = 0, 0, 0, 0
                top = idx - n_columns
                bottom = idx + n_columns
                left = idx - 1
                right = idx + 1
                
                if i == 0:
                    top = n_columns*(n_rows-1) + j
                if i == n_rows-1:
                    bottom = j;
                if j == 0:
                    left = idx + n_columns - 1
                if j == n_columns-1:
                    right = idx - n_columns + 1

                self.mol_list[idx].vibrate( [self.mol_list[left], self.mol_list[right], self.mol_list[bottom], self.mol_list[top]], k, gamma, dt, WIDTH, HEIGHT)

    def draw_screen( self, game_window ):

        # draw windows
        game_window.fill( (  0,  0,  0) )
        for mol in self.mol_list:
            mol.draw(game_window)

        
        pygame.display.update()

def f(x,t,p):
    return p

def p(x,t,f,m):
    return f/m

def k(x,t,p,f,h):
    return h*p(x,y,p,h)

def x_n_1(x,t,h):
    k1 = k*(t,x)
    k2 = k*(t + h/2,x + k1/2)
    k3 = k*(t + h/2,x + k2/2)
    k4 = k*(t + h,x + k3)

    return x + 1/6* (k1 + k2 + k3 + k4)


def calc_avg_speed( mol_list ):
    avg1 = 0
    avg2 = 0
    avg3 = 0
    N = len(mol_list)

    for mol in mol_list:
        avg1 += ( mol.vx**2 + mol.vy**2)**0.5
        avg2 += mol.vx
        avg3 += mol.vy
    avg1 /= N
    avg2 /= N
    avg3 /= N

    print("Avg Speed: ", round(avg1, 3), " Avg v in x: ", round(avg2, 3), " Avg v in y: ", round(avg3, 3))