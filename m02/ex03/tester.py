from load_csv import load
from projection_life import display


def main():
    try:
        life = load("life_expectancy_years.csv")
        gdp = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        display(life, gdp)
    except AssertionError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
