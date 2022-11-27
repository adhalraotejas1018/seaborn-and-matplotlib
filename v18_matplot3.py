# creating the subplots

import matplotlib.pyplot as plt
x =[1,2,3,4,5]
y =[1,4,9,16,25]

# plt.subplot(number of rows, number of cols, plot_number)
# means 6 part of one chart

plt.subplot(2,3,1)
plt.plot(x, y, 'r--')      # More on color options later
plt.subplot(2,3,5)
plt.plot(y, x, 'g*-')
plt.subplot(2,3,3)
plt.plot(x, y, 'r+')

plt.show()