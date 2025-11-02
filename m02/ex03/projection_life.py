import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def true_value(val):
    """Return the numeric value of a population string."""
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
    try:
        assert isinstance(life, pd.DataFrame) \
            and isinstance(gdp, pd.DataFrame), \
            "Input must be pandas DataFrames."
        assert not life.empty and not gdp.empty, \
            "One or both DataFrames are empty."
        assert 'country' in life.columns and 'country' in gdp.columns, \
            "Missing 'country' column."

        assert '1900' in gdp.columns, "Missing '1900' column in GDP data."
        gdp1900 = gdp[['country', '1900']]
        assert '1900' in life.columns, \
            "Missing '1900' column in life expectancy data."
        life1900 = life[['country', '1900']]

        df = pd.merge(gdp1900, life1900,
                      on='country', suffixes=('_gdp', '_life'))

        plt.scatter(df['1900_gdp'], df['1900_life'])
        plt.xscale('log')
        plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])
        plt.xlabel("Gross Domestic Product")
        plt.ylabel("Life Expectancy")
        plt.title("1900")

        plt.show()
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except TypeError as e:
        print(f"TypeError: {e}")
    except ValueError as e:
        print(f"ValueError: {e}")
    except KeyboardInterrupt:
        plt.close()


def main():
    life = load("life_expectancy_years.csv")
    gdp = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    display(life, gdp)


if __name__ == "__main__":
    main()
