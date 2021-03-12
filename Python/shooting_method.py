import numpy as np
import matplotlib.pyplot as plt

class ShootingMethod(object):
    def __init__(self, E_guess, potential, domain: tuple, n_points: int, boundary_conditions: dict):
        self.x = np.arange(domain[0], domain[1], (domain[1]-domain[0])/n_points)
        self.domain = domain
        self.n_points = n_points
        self.E_guess = E_guess
        self.psi = np.zeros(len(self.x))
        self.process_boundary_conditions(boundary_conditions)
        self.dx = (domain[1]-domain[0])/n_points
        self.e = 2*9.11e-31*self.E_guess/(6.5821e-16)**2 
        self.V = potential

    def get_x_idx(x):
        return np.around()

    def process_boundary_conditions(self, boundary_conditions):
        print(boundary_conditions)
        for cond in boundary_conditions.keys():
            if boundary_conditions[cond] == "function_value":
                print(cond)
                print(cond[0])
                psi_idx = np.where(np.isclose(self.x, cond[0]))
                self.psi[psi_idx] = cond[1]

    def f(self, x, y, v):
        return v
    
    def g(self, x, y, v):
        return (self.V(x) - self.e)*y

    def calculate(self):
        y'' = f y
        v = y'
        v' = f y

        for i in range(1, self.n_points):
            k0 = self.dx*self.f(self.x[i], self.psi[i], self.dpsi[i])
            l0 = self.dx*self.g(self.x[i], self.psi[i], self.dpsi[i])
            k1 = self.dx*self.f(self.x[i] + dx/2, self.psi[i] + , self.dpsi[i])
            l1 = self.dx*self.g(self.x[i] + dx/2, self.psi[i], self.dpsi[i])
            k2 = self.dx*self.f(self.x[i] + dx/2, self.psi[i], self.dpsi[i])
            l2 = self.dx*self.g(self.x[i] + dx/2, self.psi[i], self.dpsi[i])





        print(self.psi)
        for i in range(self.n_points-2):
            self.psi[i+2] = self.psi[i+1] + self.psi[i]*(2 + self.dx**2 * (self.e - self.V(self.x[i])))

    def plot(self):
        potential = np.zeros(len(self.x))
        for i in range(len(potential)):
            potential[i] = self.V(self.x[i])
        
        plt.plot(self.x, self.psi)
        plt.plot(self.x, potential)
        plt.plot(self.x, self.e*np.ones(len(potential)))
        plt.ylim(-100,100)

        plt.show()

def V(x):
    if x < -1:
        return 0
    if x > 1:
        return 0
    else:
        return -2*9.11e-31*20/(6.5821e-16)**2 

boundary_conditions = dict()
boundary_conditions[(-10, 0.00001)] = "function_value"
boundary_conditions[(-10 + 0.02, 0.0001)] = "function_value"
sm = ShootingMethod(21, V, (-10, 10), 1000, boundary_conditions)
sm.calculate()
sm.plot()
    