import matplotlib.pyplot as plt
x =[1,2,3,4,5]
y =[5,10,15,20,25]

# x is x-axis datapoints and
# y is y-axis datapoints    and -- is design of the chart

plt.plot(x,y,'-')
plt.show()
plt.plot(x,y,'--')    #graph design -- default color blue


# plt.plot(x,y,'--')    #adding r in front of -- and then color becomes red
#
# plt.plot(x,y,'r')     #red line
# plt.plot(x,y,'r+')    #red + sign
# plt.plot(x,y,'+')     #blue + sign

