#!/usr/bin/python3
"""
Technical Interview Challenge: Checks if a key can unlock all the boxes
"""


def canUnlockAll(boxes):
    # Start with the first box, which is unlocked by default
    checkList = [0]

    for box_index in checkList:
        for key in boxes[box_index]:
            if key < len(boxes) and key not in checkList:
                checkList.append(key)

    return len(checkList) == len(boxes)
