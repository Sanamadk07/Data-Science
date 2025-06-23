import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report





#Load Titanic Dataset (built-in Seaborn dataset)
titanic = sns.load_dataset("titanic")
titanic.head()


#  3. Data Preprocessing
# Select important features
df = titanic[['survived', 'pclass', 'sex', 'age']]
df = df.dropna()  # Drop rows with missing age

# Convert 'sex' column to numeric
df['sex'] = df['sex'].map({'male': 0, 'female': 1})

# Separate features (X) and target (y)
X = df[['pclass', 'sex', 'age']]
y = df['survived']



#  4. Split Data into Train and Test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)



#  4. Split Data into Train and Test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)



#  4. Split Data into Train and Test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)




#  6. Predict and Evaluate
y_pred = model.predict(X_test)

# Accuracy
print(" Accuracy:", accuracy_score(y_test, y_pred))

# Classification Report
print("📊 Classification Report:\n", classification_report(y_test, y_pred))



#  7. Try Predicting One Example
sample = pd.DataFrame({
    'pclass': [3],     # 3rd class
    'sex': [0],        # male
    'age': [22]        # 22 years old
})
prediction = model.predict(sample)
print("🎯 Prediction (1=Survived, 0=Did not survive):", prediction[0])
