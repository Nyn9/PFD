import sys


def ft_filter(function, iterable):
    """
    Returns an iterator that yields the items from the iterable
    for which function(item) returns True.
    """
    try:
        if not hasattr(iterable, '__iter__'):
            raise TypeError(f"'{type(iterable).__name__}' \
object is not iterable")
        if function is None:
            return (item for item in iterable if item)
        return (item for item in iterable if function(item))
    except TypeError as e:
        print(f"TypeError: {e}")
        sys.exit(1)


def main():
    """Example usage of ft_filter function."""
    data = [1, 2, 3, 4, 5]
    n = 5
    print(list(ft_filter(lambda x: x > 2, data)))
    print(list(ft_filter(lambda x: x > 2, n)))


if __name__ == "__main__":
    main()
