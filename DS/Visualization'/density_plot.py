import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Sample data: Random values following a normal distribution
data = np.random.normal(loc=0, scale=1, size=1000)  # Mean=0, Std Dev=1, 1000 samples

# Create the density plot with the updated fill parameter
sns.kdeplot(data, fill=True, color='green')

# Add title and labels
plt.title('Density Plot of Normally Distributed Data')
plt.xlabel('Value')
plt.ylabel('Density')

# Show the plot
plt.show()