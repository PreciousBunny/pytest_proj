from utils.arrs import get, my_slice
import pytest


def test_get():
    assert get([1, 2, 3], 1, "test") == 2
    assert get([], -1, "test") == "test"
    with pytest.raises(IndexError):
        get([], 0, "test")


def test_slice():
    assert my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert my_slice([1, 2, 3], 1) == [2, 3]


@pytest.fixture
def _array():
    return [1, 2, 3, 4, 5]

def test_my_slice_empty():
    assert my_slice([]) == []


def test_my_slice_start_opening(_array):
    assert my_slice(_array, start=3) == [ 4, 5]


def test_my_slice_reverse_start_opening(_array):
    assert my_slice(_array, start=-3) == [3, 4, 5]


def test_my_slice_reverse_start_opening_and_another_arguments(_array):
    assert my_slice(_array, start=-3, end=-1) == [3, 4]

def test_my_slice_default(_array):
    assert my_slice(_array) == _array



def test_my_slice_basis_start(_array):
    assert my_slice(_array, start=-len(_array) - 1) == my_slice(_array)