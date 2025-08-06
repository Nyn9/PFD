from give_bmi import give_bmi, apply_limit


def main():
    """Main function to test BMI calculations and limits."""
    height = [2.71, 1.15]
    weight = [165.3, 38.4]

    bmi = give_bmi(height, weight)

    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()
