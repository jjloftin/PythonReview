from matplotlib import pyplot as plt
from matplotlib import style 

##style.use('ggplot')


x = [5,6,7,8]
y = [7,3,8,3]

x2 = [5,6,7,8]
y2 = [2,5,9,6]

plt.plot(x,y, 'g', linewidth=5) # 'g' = green
plt.plot(x2,y2, 'c', linewidth=10) # 'c' = cyan
plt.title('Chart Example')
plt.ylabel('y-axis')
plt.xlabel('x-axis')

plt.show()
