# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

# -------------------------------
# 1. NumPy Array and Mean
# -------------------------------
arr = np.arange(1, 11)  # numbers from 1 to 10
mean_value = np.mean(arr)
print("NumPy Array:", arr)
print("Mean:", mean_value)

# -------------------------------
# 2. Pandas DataFrame and Summary
# -------------------------------
# Create a small dataset
data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Age": [25, 30, 35, 40],
    "Score": [88, 92, 95, 70]
}
df = pd.DataFrame(data)

print("\nPandas DataFrame:")
print(df)

print("\nSummary Statistics:")
print(df.describe())

# -------------------------------
# 4. Matplotlib Line Graph
# -------------------------------
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]

plt.plot(numbers, squares, marker="o")
plt.title("Number vs. Square")
plt.xlabel("Number")
plt.ylabel("Square")
plt.grid(True)
plt.show()
