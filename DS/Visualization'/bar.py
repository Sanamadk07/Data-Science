import pandas as pd
import numpy as np
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
data=[27,45,36,18,72,81,108,19,91,105]
name=['a','b','c','d','e','f','g','h','i','j']
plt.bar(name,data)
plt.title('bar chart')
plt.show()