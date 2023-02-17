from class_customiterator import CustomIterator


if __name__ == "__main__":
    sequence = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    start_index = 3
    end_index = 8
    iter_custom = CustomIterator(sequence, start_index, end_index)

    for value in iter_custom:
        print(value)
