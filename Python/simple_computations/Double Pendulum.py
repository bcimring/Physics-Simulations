#########################################
# double penduum simulation             #
#########################################

import pygame
import math as m

pygame.init()
WIDTH = 1000
HEIGHT = 750

game_window = pygame.display.set_mode((WIDTH,HEIGHT))

def draw_screen( theta1, theta2, l1, l2 ):
    game_window.fill( (  0,  0,  0) )
    x11 = WIDTH/2
    y11 = 200

    x12 = x11 + l1*m.sin(theta1) 
    y12 = y11 + l1*m.cos(theta1) 

    x21 = x12
    y21 = y12

    x22 = x21 + l2*m.sin(theta2)
    y22 = y21 + l2*m.cos(theta2)
    
    
    pygame.draw.line(game_window, ( 255, 255, 255 ), (x11,y11), (x12, y12), 3)
    pygame.draw.line(game_window, ( 255, 255, 255 ), (x21,y21), (x22, y22), 3)

    pygame.draw.circle(game_window, ( 255, 255, 255), (int(x12), int(y12)), 10, 0)
    pygame.draw.circle(game_window, ( 255, 255, 255), (int(x22), int(y22)), 10, 0)

    
    pygame.display.update()

def time_evolve_r_k( x_in, y_in, h ):
    dydx = [0]*4
    dydxt = [0]*4
    yt = [0]*4
    k1 = [0]*4
    k2 = [0]*4
    k3 = [0]*4
    k4 = [0]*4
    yout = [0]*4

    dydx = f( x_in, y_in, dydx )
    for i in range(4):
        k1[i] = h*dydx[i]
        yt[i] = y_in[i] + 0.5*k1[i]

    dydxt = f( x_in + 0.5*h, yt, dydxt)
    for i in range(4):
        k2[i] = h*dydxt[i]
        yt[i] = y_in[i] + 0.5*k2[i]

    dydxt = f( x_in + 0.5*h, yt, dydxt)
    for i in range(4):
        k3[i] = h*dydxt[i]
        yt[i] = y_in[i] + k3[i]

    dydxt = f( x_in + h, yt, dydxt )
    for i in range(4):
        k4[i] = h*dydxt[i]
        yout[i] = y_in[i] + k1[i]/6.0 + k2[i]/3.0 + k3[i]/3.0 + k4[i]/6.0


    return yout

def f( x_in, yin, dydx ):
    dydx[0] = yin[1] # derivatives of theta1, theta2 are just
    dydx[2] = yin[3] # omega 1 and omega 2 previously


    # expression for omega 1 and 2, found with algebra manipulator
    dydx[1] = (m2*l1*yin[1]**2*m.sin(yin[2]-yin[0])*m.cos(yin[2]-yin[0]) +
               m2*g*m.sin(yin[2])*m.cos(yin[2]-yin[0]) + m2*l1*yin[3]**2*m.sin(yin[2]-yin[1])
               - (m1 + m2)*g*m.sin(y[0]))
    dydx[1] /= ( (m1 + m2)*l1 -m2*l1*m.cos(yin[2]-yin[0])**2)

    dydx[3] = - m2*l2*yin[3]**2*m.sin(yin[2]-yin[0])*m.cos(yin[2]-yin[0]) + (m1 + m2)*(g*m.sin(yin[0])*m.cos(yin[2]-yin[0])
              - l1*yin[1]**2*m.sin(yin[2]-yin[0])
              - g*m.sin(yin[2]))
    dydx[3] /= ( (m1 + m2)*l2 -m2*l2*m.cos(yin[2]-yin[0])**2)

    return dydx

    
theta1 = 0
theta2 = 3.14
omega1 = 00
omega2 = 0
y = [theta1, omega1, theta2, omega2]
x = 0

m1 = 100
m2 = 50
g = 300
l1 = 200
l2 = 200
del_t = 0.01


Ei = 1/2*m1*l1**2*omega1**2 + 1/2*m2*l2**2*omega2**2 + m1*g*l1*(1-m.cos(theta1)) + m2*g*l2*(1-m.cos(theta2))


while True:
    y = time_evolve_r_k( x, y, del_t )
    draw_screen(y[0], y[2], l1, l2)

##    if ( 1/2*m1*l1**2*y[1]**2  > Ei ):
##        y[1] /= 10
##
##    if ( 1/2*m2*l2**2*y[3]**2  > Ei ):
##        y[3] /= 10

    if ( abs(y[0]) > 100 ):
        y[0] = 0
        
    if ( abs(y[2]) > 100 ):
        y[2] = 0

    if ( abs(y[1]) > 100 ):
        y[1] = 0
        
    if ( abs(y[3]) > 100 ):
        y[3] = 0
    
    
    x += 1







    
