import matplotlib.pyplot as plt

# Sample data

x = [1, 2, 3, 4, 5,6]

y = [2, 3, 2, 3, 4,5]

# Create scatter plot

plt.scatter(x, y, color='blue', label='Data Points')
# Add labels and title

plt.xlabel('X-axis (Independent Variable)')

plt.ylabel('Y-axis (Dependent Variable)')

plt.title('Scatter Plot Example')

plt.legend()

# Show plot

plt.show()