'''1. What is the population in the given year?
The first line of input is a year. Print the population in this year.
2. When did the world population first exceed the given population? 
The second line of input is a positive number. Print the earliest year in which the world population exceeded the given number.
3. What is the maximum value of the given field? 
The third line of input is the name of a field in the header, print the maximum value in the given field. '''

def solution():
    table = []
    
    data = open('WorldPopulation.csv', 'r')
    year = input()
    population = input()
    value = input()
    header = data.readline().strip()
    line = data.readline()
    population_year_list = []
    population_in_that_year = []
    while line:
        line = line.strip()
        columns = line.split(',')
        table.append(columns)
        line = data.readline()
    #year = input()

    for i in range(len(table)):
        if table[i][0] == year:
            population_in_that_year.append(table[i][1])
        if population < table[i][1]:
            population_year_list.append(table[i][0])
    
    #value = input()
    values = []
    for i in range(len(table)):
        if value == 'Year':
            values.append(table[i][0])
        elif value == 'Population':
            values.append(table[i][1])

        elif value == 'ChangePerc':
            values.append(table[i][2])

        elif value == 'NetChange':
            values.append(table[i][3])

        elif value == 'Density':
            values.append(table[i][4])
  
        elif value == 'Urban':
            values.append(table[i][5])
  
        elif value == 'UrbanPerc':
            values.append(table[i][6])
    #result.append(max(values))
    print('{:0.2f}'.format(int(max(values))))
    print(population_in_that_year[0])
    print(population_year_list[-1])
    data.close()
    
#print(solution())