import random
import math


# This class is about simualteed annealing.
class SimulatedAnnealing:
    
    # This function runs the simulateed annealing algorithm.
    @staticmethod
    def run(scheduler, initial_temperature, cooling_rate, iterations):
        
        current_solution = scheduler.generate_initial_solution() # Generating initial solution by using method from scheduler.
       
        current_energy = scheduler.calculate_energy(current_solution) # Calculates the energy of solution.
        
        best_solution = current_solution
        best_energy = current_energy
        
        for iteration in range(iterations): # Iteration to find best solution.
            temperature = initial_temperature * cooling_rate**iteration
            neighbor_solution = scheduler.generate_neighbor_solution(current_solution)
            neighbor_energy = scheduler.calculate_energy(neighbor_solution)

            if neighbor_energy < current_energy or random.uniform(0, 1) < pow(math.e, -(neighbor_energy - current_energy) / temperature):
                current_solution = neighbor_solution
                current_energy = neighbor_energy


            if neighbor_energy < best_energy:
                best_solution = neighbor_solution
                best_energy = neighbor_energy
              
        return best_solution
    
    