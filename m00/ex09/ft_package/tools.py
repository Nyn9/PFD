def count_in_list(lst, item):
    """
    Count the occurrences of an item in a list.

    Parameters:
    lst (list): The list to search.
    item: The item to count in the list.

    Returns:
    int: The number of times the item appears in the list.
    """
    return lst.count(item)


def main():
    """Example usage of count_in_list."""
    lst = [1, 2, 3, 1, 4, 1]
    item = 1
    count = count_in_list(lst, item)
    print(f"The item {item} appears {count} times in the list {lst}.")


if __name__ == "__main__":
    main()
