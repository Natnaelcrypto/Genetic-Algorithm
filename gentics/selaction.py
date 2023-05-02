from fitness import fitness


def selaction(population,graph):
    tested_generations=[]
    for i in population:
        fittness_of_generation=fitness(i,graph)
        tested_generations.append([i,fittness_of_generation])
    
    tested_generations.sort(key=lambda x:x[1])
    father=tested_generations[0][0]
    mother=tested_generations[1][0]

    return[father,mother],[tested_generations[0][1],tested_generations[1][1]]