from matplotlib import pyplot as plt
from matplotlib import style 

#style.use('ggplot')


x = [1,3,5,7]
y = [7,3,8,3]

x2 = [2,4,6,8]
y2 = [2,5,9,6]


plt.bar(x,y,color ='c', align='center') 
plt.bar(x2,y2,color = 'g', align='center')


plt.title('Chart Example')
plt.ylabel('y-axis')
plt.xlabel('x-axis')



plt.show()
