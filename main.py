import solver
import fileread

pizza, parameters = fileread.read_file('example.in')
results = solver.get_slices(parameters, pizza)
print results
