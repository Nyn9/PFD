def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Calculate Body Mass Index (BMI) for given height and weight."""
    bmi = []
    try:
        if not isinstance(height, list) or not isinstance(weight, list):
            raise ValueError("Height and weight must be lists.")
        if (len(height) != len(weight) or len(height) == 0):
            raise ValueError("Size incorrect.")
        for h, w in zip(height, weight):
            if not isinstance(w, (float, int)):
                raise ValueError("Weight must be a float or int.")
            if not isinstance(h, (float, int)):
                raise ValueError("Height must be a float or int.")
            if h <= 0 or w < 0:
                raise ValueError("Height must be positive \
and weight must be non-negative.")
            bmi.append(w / (h ** 2))
    except Exception as e:
        print(f"Error: {e}")
        return None
    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Apply a limit to the BMI values."""
    try:
        if not isinstance(limit, int):
            raise ValueError("Limit must be an integer.")
        if limit < 0:
            raise ValueError("Limit must be a non-negative integer.")
        if not isinstance(bmi, list) or len(bmi) == 0:
            raise ValueError("BMI must be a non-empty list.")
        for b in bmi:
            if not isinstance(b, (int, float)):
                raise ValueError("BMI values must be int or float.")
            if b < 0:
                raise ValueError("BMI values must be non-negative.")
    except Exception as e:
        print(f"Error: {e}")
        return None
    return [b > limit for b in bmi]


def main():
    """Main function to test BMI calculations and limits."""
    height = [-2.71, 1.15]
    weight = [165.3, 38.4]

    bmi = give_bmi(height, weight)

    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()
