import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def aff_life(df: pd.DataFrame):
    """Display a DataFrame as a line plot."""
    try:
        assert isinstance(df, pd.DataFrame), \
            "Input must be a pandas DataFrame."
        assert 'country' in df.columns, "Missing 'country' column."
        france = df[df['country'] == 'France']
        assert not france.empty, "No data found."
        years = df.columns[1:]
        assert all(str(y).isdigit() for y in years), \
            "Years columns must be numeric."
        values = france[years].iloc[0]
        plt.plot(years, values)
        plt.xticks(years[::40])
        plt.xlabel("Year")
        plt.ylabel("Life Expectancy")
        plt.title("France Life Expectancy Projection")
        plt.show()
    except AssertionError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"TypeError: {e}")
    except KeyboardInterrupt:
        plt.close()


def main():
    """Main function to test the display."""
    df = load("life_expectancy_years.csv")
    aff_life(df)


if __name__ == "__main__":
    main()
