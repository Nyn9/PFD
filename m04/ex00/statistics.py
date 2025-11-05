def mean(numbers: list[float]) -> float:
    """Calculate the mean of a list of numbers."""
    return sum(numbers) / len(numbers)


def median(numbers: list[float]) -> float:
    """Calculate the median of a list of numbers."""
    data = sorted(numbers)
    n = len(data)
    mid = n // 2
    if n % 2 == 0:
        return (data[mid - 1] + data[mid]) / 2
    return data[mid]


def variance(numbers: list[float]) -> float:
    """Calculate the variance of a list of numbers."""
    mn = mean(numbers)
    return sum((x - mn) ** 2 for x in numbers) / len(numbers)


def standard_deviation(numbers: list[float]) -> float:
    """Calculate the standard deviation of a list of numbers."""
    return variance(numbers) ** 0.5


def quartile(numbers: list[float]) -> list[float, float]:
    """Calculate the first and third quartiles of a list of numbers."""
    data = sorted(numbers)
    n = len(data)
    mid = n // 2
    odd = 0
    if n % 2 != 0:
        odd = 1
    first = data[:mid + odd]
    second = data[mid:]
    return [float(median(first)), float(median(second))]


def ft_statistics(*args: any, **kwargs: any) -> None:
    """Print statistical measures based on provided arguments."""
    try:
        assert all(isinstance(x, (int, float)) for x in args), \
            "All arguments must be numeric."
        if 'mean' in kwargs.values():
            if len(args) == 0:
                print("ERROR")
            else:
                print("mean:", mean(args))
        if 'median' in kwargs.values():
            if len(args) == 0:
                print("ERROR")
            else:
                print("median:", median(args))
        if 'quartile' in kwargs.values():
            if len(args) == 0:
                print("ERROR")
            else:
                print("quartile:", quartile(args))
        if 'std' in kwargs.values():
            if len(args) == 0:
                print("ERROR")
            else:
                print("std:", standard_deviation(args))
        if 'var' in kwargs.values():
            if len(args) == 0:
                print("ERROR")
            else:
                print("var:", variance(args))
    except AssertionError as e:
        print("AssertionError:", e)


def main():
    """Main function to test statistical calculations."""
    print("Statistics Tests:")
    ft_statistics(1, 2, 3, 4, 5, measure='mean')
    ft_statistics(1, 2, 3, 4, 5, measure='median')
    ft_statistics(1, 2, 3, 4, 5, measure='quartile')
    ft_statistics(1, 2, 3, 4, 5, measure='std')
    ft_statistics(1, 2, 3, 4, 5, measure='var')

    # ----- #

    ft_statistics(measure='mean')
    ft_statistics(measure='median')
    ft_statistics(measure='quartile')
    ft_statistics(measure='std')
    ft_statistics(measure='var')

    # ----- #

    ft_statistics(1, 'a', 3, measure='mean')
    ft_statistics(1, 2, None, measure='median')


if __name__ == "__main__":
    main()
