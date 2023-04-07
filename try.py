import matrix
lst=matrix.Matrix(2,3)

for i in range(100000):
    print(lst.data)
    lst.randomize(start=-0.1,end=0.1)
    lst.tanh()