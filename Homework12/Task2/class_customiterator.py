from typing import Any, List


class CustomIterator:
    """
    An iterator that iterates through a sequence of values within a specified range.

    Attributes:
        sequence (List[Any]): The sequence to iterate through.
        current_index (int): The index of the current element in the sequence.
        end_index (int): The index of the end of the range to iterate through.
    """
    def __init__(self, sequence: List[Any], start_index: int, end_index: int):
        """
        Constructor for the CustomIterator class.

        Args:
            sequence (List[Any]): The sequence to iterate through.
            start_index (int): The index of the start of the range to iterate through.
            end_index (int): The index of the end of the range to iterate through.
        """
        self.sequence = sequence
        self.current_index = start_index
        self.end_index = end_index
    
    def __iter__(self):
        """
        Returns the iterator.

        Returns:
            CustomIterator: The iterator.
        """
        return self
    
    def __next__(self):
        """
        Returns the next element in the sequence.

        Returns:
            Any: The next element in the sequence.

        Raises:
            StopIteration: If the end of the sequence has been reached.
        """
        if self.current_index < self.end_index:
            result = self.sequence[self.current_index]
            self.current_index += 1
            return result
        else:
            raise StopIteration
