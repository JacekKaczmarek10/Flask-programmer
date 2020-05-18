def add(x, y=2):
    return x + y

def product (x, y=2):
    return x * y

for i in range(3):
    for j in range(2):
        print(j)

for i in range(1,11):
    print('{:<3}|'.format(i),end="")

    for j in range(1,11):
        print('{:>4}'.format(i * j),end="")
    
    if i == 1:
        print('\n{:#^44}'.format(""),end="")
    
    print("")

    condition = 10

    while condition != 0: 
        print(condition)
        condition = condition - 1


for i in range(1,11):
    if i == 5:
        break
    print(i)