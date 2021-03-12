import numpy as np
import matplotlib.pyplot as plt

class ShootingMethod(object):
    def __init__(self, E_guess, potential, domain: tuple, n_points: int, boundary_conditions: dict):
        self.x = np.arange(domain[0], domain[1], (domain[1]-domain[0])/n_points)
        self.domain = domain
        self.n_points = n_points
        self.E_guess = E_guess
        psi = np.zeros(len(x))
        self.process_boundary_conditions(boundary_conditions)

    def get_x_idx(x):
        return np.around()

    def process_boundary_conditions(self, boundary_conditions):
        for cond in boundary_conditions.keys():
            if cond == "function_value":


    def calculate(self):
