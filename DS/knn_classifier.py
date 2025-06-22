import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

data_knn = {
    "Age": [25, 34, 17, 29, 120, -5, 30, 40, 50, 60],
    "BMI": [20, 22, 18, 24, 30, 16, 21, 35, 38, 40],
    "Class": [0, 1, 0, 1, 1, 0, 1, 1, 0, 0]
}
df_knn = pd.DataFrame(data_knn)
X = df_knn[['Age', 'BMI']]
y = df_knn['Class']
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)
predicted_class = knn.predict([[40, 43.6]])
print(f"Predicted class for BMI=43.6 and Age=40: {predicted_class[0]}")