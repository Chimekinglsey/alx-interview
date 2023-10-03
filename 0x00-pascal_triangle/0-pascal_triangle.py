#!/usr/bin/python3
"""
0-pascal_triangle: This module provides a function to generate
    Pascal's Triangle based on input
"""


def pascal_triangle(n):
    if not isinstance(n, int) or n <= 0:
        return []
    myList = [[1]]
    count = 1
    while (n > count):
        prev_row = myList[-1]
        curr_row = [1]
        i = 1
        while len(prev_row) > i:
            curr_row.append(prev_row[i-1]+ prev_row[i])
            i += 1
        curr_row.append(1)
        myList.append(curr_row)
        count += 1
    return myList