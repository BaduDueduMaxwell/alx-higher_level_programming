#!/usr/bin/python3
"""Defines a peak-finding algorithm /function"""


def find_peak(list_of_integers):
    """ Recursion using Binary Search """
    if not list_of_integers:
        return None

    def binary_search_peak(low, high):
        """Perform binary search to find a peak in the list."""
        if low == high:
            return list_of_integers[low]

        mid = (low + high) // 2

        if list_of_integers[mid] >= list_of_integers[mid + 1]:
            return binary_search_peak(low, mid)
        return binary_search_peak(mid + 1, high)

    return binary_search_peak(0, len(list_of_integers) - 1)
