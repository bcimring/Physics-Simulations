##########################################################
# This is a simulation of a string with applied tension  #
# simulating wave phenomena                              #
##########################################################

import pygame
import math as m

pygame.init()
WIDTH = 1000
HEIGHT = 500

game_window = pygame.display.set_mode((WIDTH,HEIGHT))

def draw_screen( u ):
    game_window.fill( ( 0, 0, 0) )

    for i in range(len(u)):
        pygame.draw.circle(game_window, (   0, 250, 255), ( i, int(HEIGHT/2 + u[i].real )), 1 )

    pygame.display.update()
  
def time_evolve_p_d( u, C, K, V ):
    # the next time step of psi
    u_pos = [0 for i in range(len(u)) ]

    for i in range(1,len(u)-1):
        u_pos[i] = u[i] + C*( u[i-1] + u[i+1] - 2*u[i] ) - K*V[i]*u[i]

    # enforce boundary conditions
    u_pos[0] = 0
    u_pos[len(u)-1] = 0

    # change timestep
    u = u_pos
        
    return u_pos

def init_function( u ):
    for i in range(len(u)):
        u[i] = complex( 50*2.71718**(-(i-WIDTH/2 - WIDTH/10)**2/50000), 0)

        # some example initial wave functions
        # wave packet: complex( 20*2.71718**(-(i-WIDTH/2 + WIDTH/6)**2/50000), 0)
        # sinusoid: complex(50*m.sin(m.pi*i/WIDTH), 0)

    return u

def potential_function( V ):
    for i in range(len(u)):
        V[i] = abs(i-WIDTH/2)

        # some example simulations:
        
        # absolute potential: abs(i-WIDTH/2)
        # cool anmation: complex(100*m.atan((i-WIDTH/2)/100), 0)
        # harmonic potential: V[i] = complex(100*HEIGHT/WIDTH**2 * (i- WIDTH/2)**2 - HEIGHT/2, 0)

    return V

def renormalize( u, N ):
    # make sure the amplitudes dont go out of control
    N_curr = 0;
    for i in range(WIDTH):
        N_curr += u[i]
    N_curr /= WIDTH

    for i in range(WIDTH):
        u[i] *= N/N_curr

    return u
    

# psi is u and V is the potential 
u = []
for i in range(WIDTH):
    u.append(complex(0, 0))
V = u[:]


# parameters
dt = 0.00000005
dx = 0.005
h = 0.001

C = complex(0, h*dt/dx**2) # C = i*h*dt/2pi*dx^2
K = complex(0, dt/h) # K = i*dt*2pi/h

# create the initial functions
u = init_function( u )
V = potential_function( V )

# normalize (needs work)
N = 0;
for i in range(WIDTH):
    N += u[i]
N /= WIDTH


draw_screen(u)
while True:
    # display real part of wave funciton
    draw_screen(u)
    
    # time evolve wave function
    u = time_evolve_p_d(u, C, K, V)
    
    # renormalize due to instability
    #u = renormalize( u, N )
