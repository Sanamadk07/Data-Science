import numpy as np

# Original dataset
data = {
    "Feature1": (10, 20, 30, 40, 50),
    "Feature2": [100, 200, 300, 400, 500],
    "Feature3": [5, 15, 25, 35, 45]
}

# Min-Max Normalization
min_max_normalized_data = {
    "Feature1": [(x - 20) / (50 - 20) for x in data["Feature1"]],
    "Feature2": [(x - 100) / (500 - 100) for x in data["Feature2"]],
    "Feature3": [(x - 5) / (45 - 5) for x in data["Feature3"]]
}

# Z-Score Normalization
z_score_normalized_data = {
    "Feature1": [(x - 36) / np.std(data["Feature1"]) for x in data["Feature1"]],
    "Feature2": [(x - 300) / np.std(data["Feature2"]) for x in data["Feature2"]],
    "Feature3": [(x - 25) / np.std(data["Feature3"]) for x in data["Feature3"]]
}

# Decimal Scale Normalization
decimal_scale_normalized_data = {
    "Feature1": [x / 10**2 for x in data["Feature1"]],
    "Feature2": [x / 10**3 for x in data["Feature2"]],
    "Feature3": [x / 10**2 for x in data["Feature3"]]
}

# Displaying the results
print("Min-Max Normalized Data:")
print(min_max_normalized_data)
print("\nZ-Score Normalized Data:")
print(z_score_normalized_data)
print("\nDecimal Scale Normalized Data:")
print(decimal_scale_normalized_data)
