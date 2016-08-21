from matplotlib import pyplot as plt
from matplotlib import style 
import numpy

style.use('ggplot')

x,y = numpy.loadtxt('exampleFile.csv', unpack=True, delimiter = ',')

plt.plot(x,y)

plt.title('Chart Example')
plt.ylabel('y-axis')
plt.xlabel('x-axis')



plt.show()
