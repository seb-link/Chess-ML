import numpy

data = numpy.load('y_train',allow_pickle=True)

for i in data :
    print(i)