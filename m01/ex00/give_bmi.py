import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Calculate Body Mass Index (BMI) for given height and weight."""
    try:
        if not isinstance(height, list) or not isinstance(weight, list):
            raise ValueError("Height and weight must be lists.")
        if (len(height) != len(weight) or len(height) == 0):
            raise ValueError("Size incorrect.")
        h_arr = np.array(height)
        w_arr = np.array(weight)
        if not np.issubdtype(h_arr.dtype, np.number) \
                or not np.issubdtype(w_arr.dtype, np.number):
            raise ValueError("Height and weight must contain numeric values.")
        if np.any(h_arr <= 0) or np.any(w_arr <= 0):
            raise ValueError("Height and Width must be positive.")
        bmi_arr = w_arr / (h_arr ** 2)
        return bmi_arr.tolist()
    except Exception as e:
        print(f"Error: {e}")
        return None


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Apply a limit to the BMI values."""
    try:
        if not isinstance(limit, int):
            raise ValueError("Limit must be an integer.")
        if limit < 0:
            raise ValueError("Limit must be a non-negative integer.")
        if not isinstance(bmi, list) or len(bmi) == 0:
            raise ValueError("BMI must be a non-empty list.")
        bmi_arr = np.array(bmi)
        if not np.issubdtype(bmi_arr.dtype, np.number):
            raise ValueError("BMI values must be numeric.")
        if np.any(bmi_arr < 0):
            raise ValueError("BMI values must be non-negative.")
        result_arr = bmi_arr > limit
        return result_arr.tolist()
    except Exception as e:
        print(f"Error: {e}")
        return None


def main():
    """Main function to test BMI calculations and limits."""
    height = [-2.71, 1.15]
    weight = [165.3, 38.4]

    bmi = give_bmi(height, weight)

    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()
