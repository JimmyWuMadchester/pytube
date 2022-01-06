import pytest


def max_subarray(arr: list):
    """
    max(max_subarray(arr[0:-2]), arr[i,-1])
    :param arr: 
    :return: 
    """
    i, j = None, None
    if len(arr) == 0:
        return i, j, 0
w
    sub_sum = 0
    sub_i = 0
    max_sum = -1

    for idx, item in enumerate(arr):
        sub_sum += item
        if sub_sum > max_sum:
            i = sub_i
            j = idx
            max_sum = sub_sum

        if sub_sum < 0:
            sub_sum = 0
            sub_i = idx + 1

    return i, j, max_sum


@pytest.mark.parametrize("arr, expected",
                         [
                             pytest.param(
                                 [1, 1, 1, 1], 4
                             ),
                             pytest.param(
                                 [1, -2, 1, 2, 3, -4], 6
                             ),
                             pytest.param(
                                 [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7], 43
                             )
                         ])
def test_max_subarray(arr: list, expected: int):
    i, j, max_sum = max_subarray(arr)
    print(f"max sum starts from {i} until {j} => {max_sum}")
    assert max_sum == expected
