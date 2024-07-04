#!/usr/bin/python3

"""
Provides a function to find a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    Finds a peak element in a lis tof unsorted integers.

    A peak element is an elment that is greater than or equal to its neighbors.
    For the elements at the edges of the list, only one neighbor is considered.

    Args:
        list_of_integers (list): A list of unsorted integers.

    Returns:
        int: A peak element from the list. If the list is empty, returns None.
    """
    if not list_of_integers:
        return None

    def find_peak_util(nums, low, high):
        if low == high:
            return nums[low]

        mid = (low + high) // 2

        if nums[mid] < nums[mid + 1]:
            return find_peak_util(nums, mid + 1, high)
        else:
            return find_peak_util(nums, low, mid)

    return find_peak_util(list_of_integers, 0, len(list_of_integers) - 1)
