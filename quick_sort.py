import random

import pytest


def randomized_partition(arr: list, p: int, r: int):
    """
    Use random sampling be get reasonably well balanced splits
    :param arr: 
    :param p: 
    :param r: 
    :return: 
    """
    i = random.randint(p, r)
    arr[i], arr[r] = arr[r], arr[i]
    return partition(arr, p, r)


def partition(arr: list, p: int, r: int):
    """
    Use x = arr[r] as a pivot and find its new index i so arr[p:i-1] <= x and x <=arr[i+1:r]
    :param arr: 
    :param p: 
    :param r: 
    :return: 
    """

    x = arr[r]
    i = p - 1

    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[r] = arr[r], arr[i + 1]

    return i + 1


def quicksort(arr: list, p: int, r: int):
    if p < r:
        q = randomized_partition(arr, p, r)
        quicksort(arr, p, q - 1)
        quicksort(arr, q + 1, r)


def tail_recursive_quicksort(arr: list, p: int, r: int):
    while p < r:
        # Partition and sort left subarray
        q = randomized_partition(arr, p, r)
        tail_recursive_quicksort(arr, p, q - 1)
        p = q + 1


@pytest.mark.parametrize("arr, expected, expected_q",
                         [
                             pytest.param(
                                 [5, 2, 4, 7, 1, 3, 2, 6], [5, 2, 4, 1, 3, 2, 6, 7], 6
                             ),
                             pytest.param(
                                 [2, 8, 7, 1, 3, 5, 6, 4], [2, 1, 3, 4, 7, 5, 6, 8], 3
                             ),
                             pytest.param(
                                 [1, 1, 1, 1], [1, 1, 1, 1], 3
                             ),
                         ])
def test_partition(arr: list, expected: list, expected_q: int):
    q = partition(arr, 0, len(arr) - 1)
    assert q == expected_q
    assert arr == expected


@pytest.mark.parametrize("arr, expected",
                         [
                             pytest.param(
                                 [5, 2, 4, 7, 1, 3, 2, 6], [1, 2, 2, 3, 4, 5, 6, 7]
                             ),
                             pytest.param(
                                 [2, 8, 7, 1, 3, 5, 6, 4], [1, 2, 3, 4, 5, 6, 7, 8]
                             ),
                             pytest.param(
                                 [1, 1, 1, 1], [1, 1, 1, 1]
                             ),
                         ])
def test_quicksort(arr: list, expected: list):
    quicksort(arr, 0, len(arr) - 1)
    assert arr == expected


@pytest.mark.parametrize("arr, expected",
                         [
                             pytest.param(
                                 [5, 2, 4, 7, 1, 3, 2, 6], [1, 2, 2, 3, 4, 5, 6, 7]
                             ),
                             pytest.param(
                                 [2, 8, 7, 1, 3, 5, 6, 4], [1, 2, 3, 4, 5, 6, 7, 8]
                             ),
                             pytest.param(
                                 [1, 1, 1, 1], [1, 1, 1, 1]
                             ),
                         ])
def test_tail_recursive_quicksort(arr: list, expected: list):
    tail_recursive_quicksort(arr, 0, len(arr) - 1)
    assert arr == expected
