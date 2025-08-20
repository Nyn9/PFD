from load_csv import load
from aff_pop import display


def main():
    try:
        csv = load("population_total.csv")
        display(csv)
    except AssertionError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
