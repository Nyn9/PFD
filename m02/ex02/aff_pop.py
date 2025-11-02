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


def display(df: pd.DataFrame):
    """Compare population projections."""
    try:
        assert isinstance(df, pd.DataFrame), \
            "Input must be a pandas DataFrame."
        assert not df.empty, "DataFrame is empty."
        assert 'country' in df.columns, "Missing 'country' column."

        france = df[df['country'] == 'France']
        assert not france.empty, "No data found for France."
        algeria = df[df['country'] == 'Algeria']
        assert not algeria.empty, "No data found for Algeria."
        morocco = df[df['country'] == 'Morocco']
        assert not morocco.empty, "No data found for Morocco."

        years = [y for y in df.columns[1:] if int(y) <= 2050]

        values_fr = france[years].iloc[0].apply(true_value)
        values_dz = algeria[years].iloc[0].apply(true_value)
        values_ma = morocco[years].iloc[0].apply(true_value)

        plt.plot(years, values_fr, label="France", color='blue')
        plt.plot(years, values_dz, label="Algeria", color='green')
        plt.plot(years, values_ma, label="Morocco", color='red')

        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.xticks(years[::40])
        max_pop = max(max(values_fr), max(values_dz), max(values_ma))
        y_ticks = [i * 2e7 for i in range(int(max_pop / 2e7) + 1)]
        plt.yticks(y_ticks, ["{:,.0f}M".format(pop / 1e6) for pop in y_ticks])
        plt.legend(loc="lower right")
        plt.title("Population Projections")
        plt.show()
    except AssertionError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"ValueError: {e}")
    except KeyboardInterrupt:
        plt.close()


def main():
    csv = load("population_total.csv")
    display(csv)


if __name__ == "__main__":
    main()
