import matplotlib.pyplot as plt
import pandas as pd


def true_value(val):
    if isinstance(val, str):
        val = val.strip()
        if val.endswith("B"):
            return float(val[:-1]) * 1_000_000_000
        elif val.endswith("M"):
            return float(val[:-1]) * 1_000_000
        elif val.endswith("k"):
            return float(val[:-1]) * 1_000
        else:
            return float(val)
    return val


def display(life: pd.DataFrame, gdp: pd.DataFrame):
    """Compare population to GDP for each country in 1900."""
    if not isinstance(life, pd.DataFrame) or not isinstance(gdp, pd.DataFrame):
        raise AssertionError("Expected a pandas DataFrame.")
    if 'country' not in life.columns or 'country' not in gdp.columns:
        raise AssertionError("Missing 'country' column.")


    gdp_1900 = gdp[['country', '1900']]
    life_1900 = life[['country', '1900']]

    df = pd.merge(gdp_1900, life_1900, on='country', suffixes=('_gdp', '_life'))

    plt.scatter(df['1900_gdp'], df['1900_life'])
    plt.xscale('log')
    plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])
    plt.xlabel("Gross Domestic Product")
    plt.ylabel("Life Expectancy")
    plt.title("1900")

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
