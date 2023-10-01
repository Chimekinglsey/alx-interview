"""
0-pascal_triangle: This module provides a function to generate
    Pascal's Triangle based on input
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the specified number of rows.

    Args:
        n (int): The number of rows to generate in Pascal's Triangle.

    Returns:
        list: A list of lists representing Pascal's Triangle.

    Example:
        >>> pascal_triangle(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
    if not isinstance(n, int) or n <= 0:
        return []

    triangle = [[1]]

    for _ in range(1, n):
        previous_row = triangle[-1]
        current_row = [1]  # First element of each row is always 1
        for i in range(len(previous_row) - 1):
            current_row.append(previous_row[i] + previous_row[i + 1])
        current_row.append(1)  # Last element of each row is always 1
        triangle.append(current_row)

    return triangle
