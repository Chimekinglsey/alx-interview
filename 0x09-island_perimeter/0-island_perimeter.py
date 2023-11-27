#!/usr/bin/python3
"""Island Perimeter Calculator
"""


def island_perimeter(grid):
    """Returns the perimeter of the island described in `grid`"""
    grid_extract = []
    max_width = 0

    for row in grid:
        firs_land_idx = None
        last_land_idx = None
        cell_index = -1
        for cell in row:
            cell_index += 1
            if cell == 1:
                if firs_land_idx is None:
                    firs_land_idx = cell_index
                else:
                    last_land_idx = cell_index
            if firs_land_idx:
                if last_land_idx is None:
                    last_land_idx = 0
                land_row = [i for i in range(firs_land_idx, last_land_idx + 1)]
                if land_row and len(land_row) > 0:
                    if len(land_row) > max_width:
                        max_width = len(land_row)
                    grid_extract.append(land_row)
    return (len(grid_extract) * max_width)
