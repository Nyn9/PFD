import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Calculate Body Mass Index (BMI) for given height and weight."""
    try:
        assert isinstance(height, list) and isinstance(weight, list), \
            "Height and weight must be lists."
        assert all(isinstance(h, (int, float)) for h in height), \
            "Height must contain numeric values."
        assert all(isinstance(w, (int, float)) for w in weight), \
            "Weight must contain numeric values."
        assert len(height) == len(weight) and len(height) > 0, \
            "Size incorrect."
        h_arr = np.array(height)
        w_arr = np.array(weight)
        assert np.all(h_arr > 0) and np.all(w_arr > 0), \
            "Height and weight must contain positive values."
        bmi_arr = w_arr / (h_arr ** 2)
        return bmi_arr.tolist()
    except AssertionError as e:
        print(f"AssertionError: {e}")


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Apply a limit to the BMI values."""
    try:
        assert isinstance(bmi, list) and len(bmi) > 0, \
            "BMI must be a non-empty list."
        assert isinstance(limit, int), "Limit must be an integer."
        assert limit >= 0, "Limit must be a non-negative integer."
        assert all(isinstance(b, (int, float)) for b in bmi), \
            "BMI values must be numeric."
        bmi_arr = np.array(bmi)
        assert np.issubdtype(bmi_arr.dtype, np.number), \
            "BMI values must be numeric."
        assert np.all(bmi_arr >= 0), "BMI values must be non-negative."
        result_arr = bmi_arr > limit
        return result_arr.tolist()
    except AssertionError as e:
        print(f"AssertionError: {e}")


def main():
    """Main function to test BMI calculations and limits."""
    print("Give BMI Tests:")
    height = [-2.71, 1.15]
    weight = [165.3, 38.4]

    give_bmi(height, weight)

    # ----- #

    height = [2.71, 1.15, 1.80]
    weight = [165.3, 38.4]

    give_bmi(height, weight)

    # ----- #
    height = []
    weight = []

    give_bmi(height, weight)

    # ----- #
    height = [0, 0]
    weight = [165.3, 38.4]

    give_bmi(height, weight)

    # ----- #
    height = ["2.71", 1.15]
    weight = [165.3, 38.4]

    give_bmi(height, weight)

    # ----- #
    print("\nApply Limit Tests:")
    bmi = [-22.5, 27.3, 30.1]

    apply_limit(bmi, 26)

    # ----- #
    bmi = 27.5

    apply_limit(bmi, 26)

    # ----- #
    bmi = ["22.5", 27.3, 30.1]

    apply_limit(bmi, 26)

    # ----- #
    bmi = [22.5, 27.3, 30.1]

    apply_limit(bmi, -5)
    # ----- #
    bmi = []

    apply_limit(bmi, 26)


if __name__ == "__main__":
    main()
