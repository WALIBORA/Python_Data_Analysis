import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

def main():
    try:
        # Load Iris dataset from sklearn
        iris = load_iris()
        # Convert to pandas DataFrame
        df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
        df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

        # Display first few rows
        print("First 5 rows of the dataset:")
        print(df.head())

        # Explore structure: data types and missing values
        print("\nData types:")
        print(df.dtypes)
        print("\nMissing values per column:")
        print(df.isnull().sum())

        # Clean dataset: fill or drop missing values (if any)
        if df.isnull().values.any():
            print("\nMissing values found. Filling missing values with column mean.")
            df.fillna(df.mean(), inplace=True)
        else:
            print("\nNo missing values found.")

        # Basic statistics of numerical columns
        print("\nBasic statistics of numerical columns:")
        print(df.describe())

        # Group by species and compute mean of numerical columns
        print("\nMean of numerical columns grouped by species:")
        print(df.groupby('species').mean())

        # Identify patterns or interesting findings
        print("\nObservations:")
        print("- Setosa species has smaller petal length and width compared to others.")
        print("- Versicolor and Virginica have larger petals, with Virginica generally largest.")

        # Set seaborn style
        sns.set(style="whitegrid")

        # 1. Line chart showing trends over index (simulate time series)
        plt.figure(figsize=(8,5))
        for species in df['species'].unique():
            subset = df[df['species'] == species]
            plt.plot(subset.index, subset['sepal length (cm)'], marker='o', label=species)
        plt.title('Sepal Length Trend by Species (Index as Time)')
        plt.xlabel('Index')
        plt.ylabel('Sepal Length (cm)')
        plt.legend(title='Species')
        plt.tight_layout()
        plt.show()

        # 2. Bar chart: average petal length per species
        plt.figure(figsize=(6,4))
        sns.barplot(x='species', y='petal length (cm)', data=df, ci=None)
        plt.title('Average Petal Length per Species')
        plt.xlabel('Species')
        plt.ylabel('Petal Length (cm)')
        plt.tight_layout()
        plt.show()

        # 3. Histogram of sepal length
        plt.figure(figsize=(6,4))
        sns.histplot(df['sepal length (cm)'], bins=20, kde=True)
        plt.title('Distribution of Sepal Length')
        plt.xlabel('Sepal Length (cm)')
        plt.ylabel('Frequency')
        plt.tight_layout()
        plt.show()

        # 4. Scatter plot: sepal length vs petal length colored by species
        plt.figure(figsize=(7,5))
        sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df, palette='deep')
        plt.title('Sepal Length vs Petal Length by Species')
        plt.xlabel('Sepal Length (cm)')
        plt.ylabel('Petal Length (cm)')
        plt.legend(title='Species')
        plt.tight_layout()
        plt.show()

    except FileNotFoundError as e:
        print(f"File not found error: {e}")
    except pd.errors.EmptyDataError as e:
        print(f"Pandas empty data error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
