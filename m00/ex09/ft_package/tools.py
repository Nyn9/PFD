# pip install --upgrade pip setuptools wheel build
def count_in_list(lst, item):
    """Count the occurrences of an item in a list."""
    try:
        count = lst.count(item)
    except AttributeError as e:
        print(f"TypeError: {e}")
        return None
    return count


def main():
    """Example usage of count_in_list."""
    try:
        lst = [1, 2, 3, 2, 4, 2]
        item = 2
        count = count_in_list(lst, item)
        print(f"The item {item} appears {count} times in the list {lst}.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
