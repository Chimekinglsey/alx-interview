#!/usr/bin/python3
"""
Technical Interview Challenge: Checks if a key can unlock all the boxes
"""
def canUnlockAll(boxes):
    """A key with same number as the box opens that box"""
    checkList = []
    if len(boxes) > 0:
        checkList.append(boxes[0]) #this is unlocked already
        for box in boxes:
            if len(box) == 0:
                 checkList.append(box)#checks each box inside the boxes
            for number in box:
                if boxes[number]:#unlocks a box
                    if not boxes[number] in checkList:
                            checkList.append(boxes[number])

    # print("checklist: ", checkList, '\nBoxes: ', boxes)
    if len(checkList) == len(boxes):
        return True
    return False