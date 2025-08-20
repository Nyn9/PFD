import matplotlib.pyplot as plt
import pandas as pd


def display(df: pd.DataFrame):
    """Display a DataFrame as a line plot."""
    if not isinstance(df, pd.DataFrame):
        raise AssertionError("Expected a pandas DataFrame.")
    if 'country' not in df.columns:
        raise AssertionError("Missing 'country' column.")
    france = df[df['country'] == 'France']
    if france.empty:
        raise AssertionError("No data found for France.")
    years = df.columns[1:]
    if not all(df[col].dtype.kind in 'fi' for col in years):
        raise AssertionError("Year columns must be numeric.")
    values = france[years].iloc[0]
    plt.plot(years, values)
    plt.xticks(years[::40])
    plt.xlabel("Year")
    plt.ylabel("Life Expectancy")
    plt.title("France Life Expectancy Projection")
    try:
        plt.show()
    except KeyboardInterrupt:
        plt.close()


def main():
    """Main function to test the display."""
    try:
        display(None)
    except AssertionError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
