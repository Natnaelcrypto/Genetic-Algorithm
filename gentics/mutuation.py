import random

def mutuation(child,rate):
    for i in range(len(child)):
        x=random.choice(child)
        y=random.choice(child)
        if random.random()<rate:
            index1=child.index(x)
            index2=child.index(y)
            child[index1],child[index2]=child[index2],child[index1]
    return child
