from load_csv import load
from aff_life import display


def main():
    try:
        csv = load("life_expectancy_years.csv")
        display(csv)
    except AssertionError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
