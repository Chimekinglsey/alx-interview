#!/usr/bin/python3
""" 0-validate_utf8.py """


def validUTF8(data):
    """ Determines if a given data set is a valid utf-8 encoding"""
    true = []
    false = []
    for item in data:
        if item > 0 and len(bin(item)) < 11:
            true.append(True)
        elif item < 0 and len(bin(item)) < 12:
            true.append(True)
        else:
            false.append(False)
    return True if len(false) == 0 else False
