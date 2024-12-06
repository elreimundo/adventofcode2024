import os

from src.solver import solve, solve_similiarity

inputs = open(os.path.join(os.path.dirname(__file__), "lists.my_data"), "r").readlines()

print(solve(inputs))
print(solve_similiarity(inputs))