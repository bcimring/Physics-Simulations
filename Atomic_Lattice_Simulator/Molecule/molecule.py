from math import acos
from math import cos
from math import sin
from math import sqrt
from math import pi
from random import randint
import pygame

class Molecule(object):
    def __init__( self, size, xi, yi, vix, viy, clr, m, idd ):
        self.radius = size
        self.m = m
        self.x = xi
        self.y = yi
        self.vx = vix
        self.vy = viy
        self.clr = clr
        self.id = idd
        self.x_l = xi 
        self.y_l = yi
        self.x_to_ev = xi
        self.y_to_ev = yi

        return

    def check_collision( self, other ):
        if (( abs( self.x - other.x ) < (self.radius + other.radius) ) and ( abs( self.y - other.y ) < (self.radius + other.radius) )):
            if ( sqrt( (self.x - other.x)**2 + (self.y - other.y )**2) < (self.radius + other.radius) ):
                return True
        return False

    def move( self, dt ):
        self.x += self.vx*dt
        self.y += self.vy*dt
        
        return

    def collide_with( self, other, dt ):
        # performs elastic collision
        # transform to rest frame of other
        V1 = [0, 0]
        V2 = [0, 0]

        delta_x_vec = [self.x-other.x, self.y-other.y]
        delta_v_vec = [self.vx-other.vx, self.vy-other.vy]

        dv_dx = delta_x_vec[0]*delta_v_vec[0] + delta_x_vec[1]*delta_v_vec[1]

        mag_delta_x = delta_x_vec[0]**2 + delta_x_vec[1]**2 
        
        self.vx = self.vx - (2*other.m*dv_dx*delta_x_vec[0])/((self.m+other.m)*mag_delta_x) 
        self.vy = self.vy - (2*other.m*dv_dx*delta_x_vec[1])/((self.m+other.m)*mag_delta_x) 

        other.vx = other.vx + (2*self.m*dv_dx*delta_x_vec[0])/((self.m+other.m)*mag_delta_x) 
        other.vy = other.vy + (2*self.m*dv_dx*delta_x_vec[1])/((self.m+other.m)*mag_delta_x) 


        self.x += self.vx*2*dt
        self.y += self.vy*2*dt
        other.x += other.vx*2*dt
        other.y += self.vy*2*dt

        return

    def keep_on_screen(self, x, y):
        if x:
            self.vx *= -1
        if y:
            self.vy *= -1

        return
    
    def draw(self, game_window):
        pygame.draw.circle(game_window, self.clr, ( int(self.x), int(self.y) ), self.radius)
        return

    def vibrate(self, neighbors, k, gamma, dt , WIDTH, HEIGHT):
        f_x = 0
        f_y = 0

        other = neighbors[0]
        f_y += k*(other.y_to_ev - self.y_to_ev)
        if other.x > self.x_to_ev:
            f_x += k*(other.x_to_ev - WIDTH - self.x_to_ev)
        else:
            f_x += k*(other.x_to_ev - self.x_to_ev)

        other = neighbors[1]
        f_y += k*(other.y_to_ev - self.y_to_ev)
        if other.x < self.x_to_ev:
            f_x += k*(other.x_to_ev + WIDTH - self.x_to_ev)
        else:
            f_x += k*(other.x_to_ev - self.x_to_ev)

        other = neighbors[2]
        f_x += k*(other.x_to_ev - self.x_to_ev)
        if other.y < self.y_to_ev:
            f_y += k*(other.y_to_ev + HEIGHT - self.y_to_ev)
        else:
            f_y += k*(other.y_to_ev - self.y_to_ev)

        other = neighbors[3]
        f_x += k*(other.x_to_ev - self.x_to_ev)
        if other.y > self.y_to_ev:
            f_y += k*(other.y_to_ev - HEIGHT - self.y_to_ev)
        else:
            f_y += k*(other.y_to_ev - self.y_to_ev) 

        self.x = (self.x_to_ev*2 - self.x_l + dt*self.x_to_ev*gamma/self.m + dt**2 * f_x/self.m)/(1+dt*gamma/self.m)
        self.y = (self.y_to_ev*2 - self.y_l + dt*self.y_to_ev*gamma/self.m + dt**2 * f_y/self.m)/(1+dt*gamma/self.m)
        self.x_l = self.x_to_ev
        self.y_l = self.y_to_ev