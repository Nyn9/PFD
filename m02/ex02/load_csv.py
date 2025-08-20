import pandas as pd
import os


def load(path: str) -> pd.DataFrame:
    """Load a CSV file into a DataFrame."""
    if not isinstance(path, str) or not path.strip():
        raise AssertionError("Path must be a non-empty string")
    if not path.endswith(".csv"):
        raise AssertionError("File must be a CSV")
    if not os.path.isfile(path):
        raise AssertionError("File does not exist")
    try:
        df = pd.read_csv(path)
    except Exception as e:
        raise AssertionError(f"Could not load CSV: {e}")
    print("Load dataset of dimensions:", df.shape)
    return df


def main():
    """Main function to load and display the CSV data."""
    try:
        print(load("Nonexisting.csv"))
    except AssertionError as e:
        print(f"Error: {e}")

    try:
        print(load("life_expectancy_years.notcsv"))
    except AssertionError as e:
        print(f"Error: {e}")

    try:
        print(load(None))
    except AssertionError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
