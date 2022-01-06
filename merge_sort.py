import pytest


def merge(arr: list, p: int, mid: int, r: int):
    left = list(arr[p:mid])
    right = list(arr[mid:r])

    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[p + i + j] = left[i]
            i += 1
        else:
            arr[p + i + j] = right[j]
            j += 1

    while i < len(left):
        arr[p + i + j] = left[i]
        i += 1

    while j < len(right):
        arr[p + i + j] = right[j]
        j += 1

    print(f"Left: {left} / Right: {right} => {arr[p:r]}")


def merge_sort(arr: list, p: int, r: int):
    if p < r - 1:
        mid = (p + r) // 2
        merge_sort(arr, p, mid)
        merge_sort(arr, mid, r)
        merge(arr, p, mid, r)


@pytest.mark.parametrize("arr, expected",
                         [
                             pytest.param(
                                 [5, 2, 4, 7, 1, 3, 2, 6, 1], [1, 1, 2, 2, 3, 4, 5, 6, 7]
                             ),
                             pytest.param(
                                 [5, 2, 4, 7, 1, 3, 2, 6], [1, 2, 2, 3, 4, 5, 6, 7]
                             ),
                             pytest.param(
                                 [], []
                             ),
                             pytest.param(
                                 [5], [5]
                             ),
                         ])
def test_merge_sort(arr: list, expected: list):
    merge_sort(arr, 0, len(arr))
    assert arr == expected
