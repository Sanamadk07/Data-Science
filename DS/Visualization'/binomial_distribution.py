import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
n = 10
p = 0.5
samples = np.random.binomial(n, p, size=1000)
sns.histplot(samples, kde=True, bins=np.arange(n + 1) - 0.5)
plt.title(f'Binomial Distribution (n={n}, p={p})')
plt.xlabel('Number of Successes')
plt.ylabel('Frequency')
plt.show()