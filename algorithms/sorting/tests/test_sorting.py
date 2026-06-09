import pytest
from hypothesis import given
from hypothesis import strategies as st

from algorithms.sorting.bubble import bubble_sort
from algorithms.sorting.merge import merge_sort
from algorithms.sorting.quick import quick_sort

# sorts that mutate the input and return None
in_place_sorts = [
    pytest.param(bubble_sort, id="bubble_sort"),
    pytest.param(quick_sort, id="quick_sort"),
]

# sorts that return a new list and leave the input untouched
returning_sorts = [
    pytest.param(merge_sort, id="merge_sort"),
]

numeric = st.one_of(st.integers(), st.floats(allow_nan=False, allow_infinity=False))


@pytest.mark.parametrize("sort_fn", in_place_sorts)
@given(arr=st.lists(numeric))
def test_in_place_sort_matches_builtin(sort_fn, arr):
    expected = sorted(arr)
    sort_fn(arr)
    assert arr == expected


@pytest.mark.parametrize("sort_fn", in_place_sorts)
def test_in_place_sort_mutates_same_object(sort_fn):
    arr = [2, 1]
    original_ref = arr
    sort_fn(arr)
    assert arr is original_ref


@pytest.mark.parametrize("sort_fn", returning_sorts)
@given(arr=st.lists(numeric))
def test_returning_sort_matches_builtin(sort_fn, arr):
    expected = sorted(arr)
    result = sort_fn(arr)
    assert result == expected


@pytest.mark.parametrize("sort_fn", returning_sorts)
def test_returning_sort_does_not_mutate_input(sort_fn):
    arr = [2, 1]
    snapshot = list(arr)
    sort_fn(arr)
    assert arr == snapshot
