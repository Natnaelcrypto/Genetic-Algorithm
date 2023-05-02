def fitness(generation,graph):
    length=0
    
    for i in range(len(generation)):
        if i==len(generation)-1:
            
            x=graph[generation[0]][generation[i]]
            return length+x
        else:
            print(generation)
            length+=graph[generation[i]][generation[i+1]]