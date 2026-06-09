import pytest

from algorithms.sorting.bubble_sort import bubble_sort


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([3, 1, 2], [1, 2, 3]),
        ([1, 2, 3], [1, 2, 3]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([3, 1, 2, 1, 3], [1, 1, 2, 3, 3]),
        ([42], [42]),
        ([], []),
        ([-3, -1, -2], [-3, -2, -1]),
        ([-1, 0, 1, -2], [-2, -1, 0, 1]),
        ([1.5, 0.1, 3.2, 2.7], [0.1, 1.5, 2.7, 3.2]),
        ([-1.5, 0.0, -0.5, 1.1], [-1.5, -0.5, 0.0, 1.1]),
    ],
)
def test_bubble_sort(arr, expected):
    bubble_sort(arr)
    assert arr == expected


def test_modifies_in_place():
    arr = [2, 1]
    original_ref = arr
    bubble_sort(arr)
    assert arr is original_ref
