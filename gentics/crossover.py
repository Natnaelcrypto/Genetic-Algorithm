import random


def crossover(parents,pro):
    father=parents[0]
    mother=parents[1]
    childe=[]
    x=int(len(father))
    for i in range(len(father)):
        childe.append("")
    count=0
    while x>=0:
        if x%2!=0:
            chromosom=random.choice(father)
            index=father.index(chromosom)
            if childe[index]==""and childe.count(chromosom)==0:
                childe[index]=chromosom
                x-=1
                
        else:
            chromosom=random.choice(mother)
            index=mother.index(chromosom)
            if childe[index]=="" and childe.count(chromosom)==0:
                childe[index]=chromosom
                x-=1
        if count==100:
            for j in range(len(childe)):
                if childe[j]=="":
                    if x%2!=0:
                        if childe.count(father[j])==0:
                            childe[j]=father[j]
                            x-=1
                        else:
                            if childe.count(mother[j])==0:
                                childe[j]=mother[j]
                            
                    else:
                        if childe.count(mother[j])==0:
                            childe[j]=mother[j]
                            x-=1
                        else:
                            if childe.count(father[j])==0:
                                childe[j]=father[j]
            x=-1

        print(childe)
        count+=1 
        for k in range(len(father)):
            if childe.count(father[k])==0:
                for l in range(len(childe)):
                    if childe[l]=="":
                        childe[l]=father[k]
                        break

    return childe

