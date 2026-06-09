import pytest
from hypothesis import given
from hypothesis import strategies as st

from algorithms.sorting.bubble import bubble_sort

sort_implementations = [
    pytest.param(bubble_sort, id="bubble_sort"),
]

numeric = st.one_of(st.integers(), st.floats(allow_nan=False, allow_infinity=False))


@pytest.mark.parametrize("sort_fn", sort_implementations)
@given(arr=st.lists(numeric))
def test_sort_matches_builtin(sort_fn, arr):
    expected = sorted(arr)
    sort_fn(arr)
    assert arr == expected


@pytest.mark.parametrize("sort_fn", sort_implementations)
def test_sort_in_place(sort_fn):
    arr = [2, 1]
    original_ref = arr
    sort_fn(arr)
    assert arr is original_ref
