import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Load a CSV file into a DataFrame."""
    try:
        assert isinstance(path, str) and path.strip(), \
            "Path must be a non-empty string"
        assert path.endswith(".csv"), "File must be a CSV"
        df = pd.read_csv(path)
        print("Load dataset of dimensions:", df.shape)
        return df
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
    except PermissionError as e:
        print(f"PermissionError: {e}")
    except pd.errors.EmptyDataError as e:
        print(f"EmptyDataError: {e}")
    except pd.errors.ParserError as e:
        print(f"ParserError: {e}")


def main():
    """Main function to test the load function."""
    load("Nonexisting.csv")
    load("empty.csv")
    load("life_expectancy_years.notcsv")
    load(None)
    load(5)


if __name__ == "__main__":
    main()
