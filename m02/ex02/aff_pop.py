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


def display(df: pd.DataFrame):
    """Compare population projections."""
    if not isinstance(df, pd.DataFrame):
        raise AssertionError("Expected a pandas DataFrame.")
    if 'country' not in df.columns:
        raise AssertionError("Missing 'country' column.")

    france = df[df['country'] == 'France']
    if france.empty:
        raise AssertionError("No data found for France.")
    algeria = df[df['country'] == 'Algeria']
    if algeria.empty:
        raise AssertionError("No data found for Algeria.")
    morocco = df[df['country'] == 'Morocco']
    if morocco.empty:
        raise AssertionError("No data found for Morocco.")

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
    plt.title("Population Projection")
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
