
import numpy as np
import pandas as pd


# 1. Create a random Pandas Series
def create_random_series(n=10, seed=42):
    rng = np.random.default_rng(seed)
    values = rng.integers(low=1, high=100, size=n)
    return pd.Series(values)


# 2. Create a Series with custom labels
def create_labeled_series(series):
    labels = [f"num_{i + 1}" for i in range(len(series))]
    return pd.Series(series.values, index=labels)


# 3. Display Series details
def describe_series(s, title="Series"):
    print(f"{title}:")
    print(s)
    print(f"\nDtype : {s.dtype}")
    print(f"Shape : {s.shape}")
    print(f"Size  : {s.size}")
    print(f"Index : {list(s.index)}")


# 4. Main program
if __name__ == "__main__":

    # Step 1: Series with default index
    series = create_random_series()
    print("STEP 1: Series with the default index")
    describe_series(series)

    # Step 2: Series with custom labels
    labeled = create_labeled_series(series)
    print("\nSTEP 2: Same values, custom labels")
    describe_series(labeled, title="Labeled Series")

    # Step 3: Basic statistics
    print("\nSTEP 3: Basic statistics")
    print(f"Minimum : {series.min()}")
    print(f"Maximum : {series.max()}")
    print(f"Mean    : {series.mean():.2f}")
    print(f"Sum     : {series.sum()}")

    # Step 4: Sort values
    print("\nSTEP 4: Sorted values (ascending)")
    print(series.sort_values().to_string())

    # Step 5: Indexing and filtering
    print("\nSTEP 5: Indexing and filtering")
    print(f"First value (series.iloc[0]) : {series.iloc[0]}")

    print("Values greater than 50:")
    print(series[series > 50].to_string())
