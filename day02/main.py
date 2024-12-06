import os

from src.solver import count_safe_reports

inputs = open(os.path.join(os.path.dirname(__file__), "reports.my_data"), "r").readlines()

print(count_safe_reports(inputs))
