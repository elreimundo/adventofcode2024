import os

from src.solver import solve

inputs = open(os.path.join(os.path.dirname(__file__), "lists.my_data"), "r").readlines()

print(solve(inputs))