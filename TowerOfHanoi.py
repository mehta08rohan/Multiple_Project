def move(a,b):
    print(f"Move disc from {a} to {b}")

def TowerOfHanoi(numberofdisc , source , aux , target):
    if numberofdisc ==0:
        pass
    else:
        TowerOfHanoi(numberofdisc-1,source,target,aux)
        move(source,target)
        TowerOfHanoi(numberofdisc -1 ,aux,source,target)



# TowerOfHanoi(3,"A","B","C")

