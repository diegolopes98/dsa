from typing import List


def quick_sort(numbers: List[int | float], left=0, right=None) -> None:
    if right is None:
        right = len(numbers) - 1

    def _pivot(left, right):
        lo = numbers[left]
        hi = numbers[right]

        mi_idx = left + (right - left) // 2  # prevents overflow on low level languages
        mi = numbers[mi_idx]

        if lo <= mi <= hi or hi <= mi <= lo:
            return mi_idx

        if mi <= lo <= hi or hi <= lo <= mi:
            return left

        return right

    def part(left, right):
        pivot = numbers[_pivot(left, right)]
        i = left - 1
        j = right + 1

        while True:
            i += 1
            while numbers[i] < pivot:
                i += 1

            j -= 1
            while numbers[j] > pivot:
                j -= 1

            if i >= j:
                break

            numbers[i], numbers[j] = numbers[j], numbers[i]

        return j

    def rec(left, right):
        if left < right:
            pi = part(left, right)
            rec(left, pi)
            rec(pi + 1, right)

    rec(left, right)
