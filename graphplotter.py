import matplotlib.pyplot as plt

x1 = [2, 4, 5]
y1 = [2, 3, 6]

plt.plot(x1, y1, color="green", linestyle='dashed', linewidth=3, marker="o", markerfacecolor='blue', markersize='2', label = 'Line 1')
plt.ylim(1, 8)
plt.xlim(1, 8)

x2 = [1, 2, 3, 4, 5]
y2 = [1, 2, 3, 4, 5,]
plt.plot(x2, y2, label = "Line 2")

plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.title('demo - Costumization')

#legend color coding lines
plt.legend()

plt.show()

left = [1,2,3,4, 5]
height = [10, 11, 23, 35, 4]

tick_label = ['one', 'two', 'three', 'five']
# plt.bar(left, height, tick_label = tick_label, width= 0.8, color = ['blue', 'orange'])
plt.plot()