##########################################################
# This is a simulation of a string with applied tension  #
# simulating wave phenomena                              #
##########################################################

import pygame
import math as m
from random import randint
# structure of each entry in pos:
# pos[i] = (x, y, vx, vy, mass, radius, colour, identity_number)

pygame.init()
WIDTH = 1000
HEIGHT = 250

game_window = pygame.display.set_mode((WIDTH,HEIGHT))

def draw_screen( u ):
    game_window.fill( ( 0, 0, 0) )

    for i in range(len(u)):
        pygame.draw.circle(game_window, (   0, 250, 255), ( i, int(125 + u[i])  ), 1 )

    pygame.display.update()

def first_evolve( u, u_i, C ):
    for i in range(1, len(u)-2):
        u[i] = u_i[i] - 0.5*C**2*(u_i[i+1] - 2*u_i[i] + u_i[i-1])

    u[0] = 0
    u[len(u)-1] = 0

    return u
                               
    
def time_evolve_p_d( u, u_neg, C ):
    u_pos = [0 for i in range(len(u)) ]

    for i in range(1,len(u)-1):
        u_pos[i] = 2*u[i] - u_neg[i] + ( u[i-1] + u[i+1] - 2*u[i] )*C**2

    u_pos[0] = 0
    u_pos[len(u)-1] = 0

    u, u_neg = u_pos, u
        
    return u, u_neg

def init_function( u ):
    for i in range(len(u)):
##        if i < 250:
##            u[i] = (abs(i-125) - 125)*m.sin(m.pi*i/250)
##        else:
##            u[i] = (2.71**(-(i-250)/1000)-1)*100*m.sin(m.pi*i/1000)
        # Generating two wave packets
        u[i] = 100*m.sin( m.pi*i/15 )*m.sin( m.pi*i/200 )*2**(-((i-500)**4/100000000 - (i-500)**2/1000000))

    
    return u

u = []
for i in range(WIDTH):
    u.append(0)
u_neg = u[:]

C = 1.00

u_neg = init_function( u_neg )
u = first_evolve(u, u_neg, C)

draw_screen(u)
while True:
    draw_screen(u)

    u, u_neg = time_evolve_p_d(u, u_neg, C)
