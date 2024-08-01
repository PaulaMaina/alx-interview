#!/usr/bin/python3
"""Determines if all boxes can be opened"""


def canUnlockAll(boxes):
    """Checks if all boxes can be opened"""
    all_boxes = len(boxes)
    checked_boxes = set([0])
    unchecked_boxes = set(boxes[0]).difference(set([0]))

    while len(unchecked_boxes) > 0:
        box_index = unchecked_boxes.pop()
        
        if not box_index or box_index >= all_boxes or box_index < 0:
            continue
        if box_index not in checked_boxes:
            unchecked_boxes = unchecked_boxes.union(boxes[box_index])
            checked_boxes.add(box_index)

        return all_boxes == len(checked_boxes)