from matplotlib import pyplot as plt
from matplotlib import style 

#style.use('ggplot')


x = [5,6,7,8]
y = [7,3,8,3]

x2 = [5,6,7,8]
y2 = [2,5,9,6]


plt.scatter(x,y,color ='c') 
plt.scatter(x2,y2,color = 'g')


plt.title('Chart Example')
plt.ylabel('y-axis')
plt.xlabel('x-axis')



plt.show()
