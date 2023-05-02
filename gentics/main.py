
import random
from crossover import crossover
from mutuation import mutuation
from selaction import selaction

graph={
    "A":{"B":10,"C":13,"D":15,"E":11,"F":3},
    "B":{"A":10,"C":6,"D":11,"E":9,"F":13},
    "C":{"B":6,"A":13,"D":5,"E":8,"F":12},
    "D":{"B":11,"C":5,"A":15,"E":7,"F":12},
    "E":{"B":9,"C":8,"D":7,"A":11,"F":6},
    "F":{"B":13,"C":12,"D":12,"E":6,"A":3},
}
population=[["B","A","F","C","E","D"],["D","F","B","A","C","E"]]
number_of_generation=100

def Gentics(graph,population,num_gen):
   
    best_gen=None
    for i in range(num_gen+1):
        selacted,score=selaction(population,graph)
        print(selacted[0],score[0])
        if best_gen==None:
            best_gen=[selacted[0],score[0]]
        else:
            if score[0]<best_gen[1]:
                best_gen=[selacted[0],score[0]]

        child1=crossover(selacted,.2)
        child2=crossover(selacted,.2)
        
        child1=mutuation(child1,.3)
        child2=mutuation(child2,.3)
        population=[]
        population.append(child1)
        population.append(child2)

        

    return best_gen

print(Gentics(graph,population,number_of_generation))







        





