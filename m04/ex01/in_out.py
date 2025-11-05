def square(x: int | float) -> int | float:
    """Return the square of a number."""
    return x ** 2


def pow(x: int | float) -> int | float:
    """Return the power of a number."""
    return x ** x


def outer(x: int | float, function) -> object:
    """Return a closure that applies the function to x repeatedly."""
    count = 0

    try:
        assert isinstance(x, (int, float)), "x must be a number."
        assert callable(function), "function must be a function."
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return lambda: None

    def inner() -> float:
        """Inner function to apply the function repeatedly."""
        nonlocal count
        res = function(x)
        for i in range(count):
            res = function(res)
        count += 1
        return res

    return inner


def main():
    """Main function to test the outer function with square and pow."""
    print("Outer Function Tests:")

    a = outer(3, square)
    print(a())
    print(a())
    print(a())

    print("-----")

    b = outer(2, pow)
    print(b())
    print(b())
    print(b())

    print("-----")

    c = outer("2", square)
    print(c())

    print("-----")

    d = outer(2, "not_a_function")
    print(d())


if __name__ == "__main__":
    main()
