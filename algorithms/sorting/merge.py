from typing import List


def merge_sort(numbers: List[int | float]) -> List[int | float]:
    def merge(left, right):
        merged = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged

    def rec(numbers):
        size = len(numbers)
        if size <= 1:
            return numbers

        mid = size // 2
        left = numbers[:mid]
        right = numbers[mid:]

        return merge(rec(left), rec(right))

    return rec(numbers)
