from typing import List


def bubble_sort(numbers: List[int | float]) -> None:
    size = len(numbers)

    for k in range(size):
        is_sorted = True
        for i in range(size - 1 - k):
            if numbers[i] > numbers[i + 1]:
                is_sorted = False
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
        if is_sorted:
            return
