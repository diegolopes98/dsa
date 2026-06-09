# DSA

Study repo for data structures and algorithms. Uses uv + mise for tooling.

## Workflow

Tests are written first, then the user implements the solution independently. **Never write or suggest implementations.** Only write tests, explain concepts, or give hints when explicitly asked.

## Tests

Use `@pytest.mark.parametrize` for multiple input/output cases. Keep identity assertions (in-place, same object) as separate test functions.

Tests must be reusable across implementations of the same contract by parametrizing the function itself:

```python
@pytest.mark.parametrize("sort_fn", [bubble_sort, merge_sort])
@pytest.mark.parametrize("arr, expected", [...])
def test_sort(sort_fn, arr, expected):
    sort_fn(arr)
    assert arr == expected
```

Use Hypothesis for property-based testing when a known-correct reference exists (e.g. `sorted()`). Capture expected state before mutation:

```python
from hypothesis import given
from hypothesis import strategies as st

@pytest.mark.parametrize("sort_fn", sort_implementations)
@given(arr=st.lists(st.one_of(st.integers(), st.floats(allow_nan=False, allow_infinity=False))))
def test_sort_matches_builtin(sort_fn, arr):
    expected = sorted(arr)
    sort_fn(arr)
    assert arr == expected
```

Hypothesis replaces manual parametrized cases. Keep identity/structural assertions as separate test functions.

## Code navigation

Prefer LSP tools (`goToDefinition`, `findReferences`, `hover`, `documentSymbol`) over `grep`/`find` for navigating Python code.
