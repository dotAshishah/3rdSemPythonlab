# 6B. LINE PLOTTING WITH LINE FORMATTING

import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[2,4,6,8,10]
plt.plot(x,y,marker='o',linestyle='-',color='b',label='Linear Function: y=2x')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Linear Plot with Line Formatting')
plt.legend()
plt.grid(True)
plt.show()