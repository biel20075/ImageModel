def calculate_list_statistics(numbers):
    """Calculate the total, average, maximum, and minimum values of a list.

    Args:
        numbers (list[float] | list[int]): A non-empty list of numbers.

    Returns:
        tuple: (total, average, maximum, minimum)
    """
    if not numbers:
        raise ValueError("A lista não pode ser vazia.")

    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)

    return total, average, maximum, minimum


def main():
    values = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
    total, average, maximum, minimum = calculate_list_statistics(values)

    print("total:", total)
    print("media:", average)
    print("maior:", maximum)
    print("menor:", minimum)


if __name__ == "__main__":
    main()
