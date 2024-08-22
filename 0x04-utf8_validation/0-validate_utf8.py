#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding"""
    num_bytes = 0
    mask1 = 1 << 7
    mask2 = 1 << 6

    for n in data:
        mask_byte = 1 << 7
        if num_bytes == 0:
            while mask_byte & n:
                num_bytes += 1
                mask_byte = mask_byte >> 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (n & mask1 and not (n & mask2)):
                return False

        num_bytes -= 1

    if num_bytes == 0:
        return True

    return False
