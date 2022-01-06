import pytest


def max_heapify(arr: list, heap_size: int, i: int):
    """
    Maintain max-heap property at node i.
    i.e. makes arr[i] "float down"
    """
    l = (i << 1) + 1
    r = (i << 1) + 2
    largest = i

    if l < heap_size and arr[l] > arr[i]:
        largest = l

    if r < heap_size and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, heap_size, largest)


def build_max_heap(arr: list):
    heap_size = len(arr)
    for i in range(heap_size // 2 - 1, -1, -1):
        max_heapify(arr, heap_size, i)


def heap_sort(arr: list):
    build_max_heap(arr)
    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, i, 0)


@pytest.mark.parametrize("arr, expected",
                         [
                             pytest.param(
                                 [4, 16, 10], [16, 4, 10]
                             ),
                             pytest.param(
                                 [], []
                             ),
                             pytest.param(
                                 [5], [5]
                             ),
                         ])
def test_max_heapify(arr: list, expected: list):
    max_heapify(arr, 0)
    assert arr == expected


@pytest.mark.parametrize("arr, expected",
                         [
                             pytest.param(
                                 [4, 16, 10], [16, 4, 10]
                             ),
                             pytest.param(
                                 [16, 4, 10, 14, 7, 9, 3, 2, 8, 1], [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
                             ),
                             pytest.param(
                                 [], []
                             ),
                             pytest.param(
                                 [5], [5]
                             ),
                             pytest.param(
                                 [1, 1, 1, 1], [1, 1, 1, 1]
                             ),
                         ])
def test_build_max_heap(arr: list, expected: list):
    build_max_heap(arr)
    assert arr == expected


@pytest.mark.parametrize("arr, expected",
                         [
                             pytest.param(
                                 [4, 16, 10], [4, 10, 16]
                             ),
                             pytest.param(
                                 [16, 4, 10, 14, 7, 9, 3, 2, 8, 1], [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]
                             ),
                             pytest.param(
                                 [], []
                             ),
                             pytest.param(
                                 [5], [5]
                             ),
                             pytest.param(
                                 [1, 1, 1, 1], [1, 1, 1, 1]
                             ),
                         ])
def test_heap_sort(arr: list, expected: list):
    heap_sort(arr)
    assert arr == expected
