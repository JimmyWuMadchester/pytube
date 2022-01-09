import pytest


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


@pytest.mark.parametrize("arr, expected",
                         [
                             pytest.param(
                                 [5, 2, 4, 7, 1, 3, 2, 6], [5, 2, 4, 1, 3, 2, 6, 7]
                             )
                         ])
def test_partition(arr: list, expected: list):
    q = partition(arr, 0, len(arr) - 1)
    assert arr == expected
