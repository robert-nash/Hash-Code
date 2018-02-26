def read_file(file_name):
    #Opening the input file
    f = open(file_name, 'r')
    first_line = f.readline()

    #Setting the input variables
    parameters = tuple(
    map(int, first_line.split(' ')))

    #Creating the pizza grid and populating it
    grid = []
    for i in range(parameters[0]):
        grid.append(f.readline().rstrip())
    f.close()
    return (grid,parameters)
