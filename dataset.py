import numpy

datax = numpy.load('x_train',allow_pickle=True)

for i in datax :
    print(i)

datay = numpy.load('y_train',allow_pickle=True)

for i in datay :
    print(i)