import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values,y_values, edgecolor= 'none', s=40, c = y_values, cmap= plt.cm.Greys)

# Set chart title and label axes
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of value', fontsize=14)

# Set size of tick labels
plt.tick_params(axis='both', labelsize=14)

# set the range for each axis.
plt.axis([0, 1100,0, 1100000])
plt.show()

plt.savefig('squares_plot.png', bbox_inches='tight')
# bbox_inches='tight' trims extra whitespace from the plot

