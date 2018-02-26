#Opening the input file
f = open('example.in', 'r')
first_line = f.readline()

#Setting the input variables
row_count, column_count, min_ingredient, max_area = tuple(
map(int, first_line.split(' ')))

#Creating the pizza grid and populating it
grid = []
for i in range(row_count):
    grid.append(f.readline().rstrip())

f.close()