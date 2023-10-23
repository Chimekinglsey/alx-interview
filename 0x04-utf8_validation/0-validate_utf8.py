#!/usr/bin/python3
""" 0-validate_utf8.py """


def validUTF8(data):
    """
    Determines if a given data set is a valid utf-8 encoding
        @valid utf-8 has 4 basic rules:
            1. If it's a single-byte (ASCII) then it's 7 bits with leading 0
                # Leading byte is most significant bit
            2. If it's a multi-byte, then:
                (a) two-bytes will have a leading 110xxxxx
                (b) three bytes will have a leading 1110xxxx
                (c) four bytes will have a leading 11110xxx
            3. If none of these conditions are met, then it's not a valid utf-8
            # Binary rep is not same as utf-8. bin(224 >> 4) REPL
    """
    leading_bytes = 0

    for item in data:
        # Check if the MSB is 0 or if it's the start of a multi-byte character.
        if leading_bytes == 0:
            if (item >> 7) == 0:
                leading_bytes = 0
            elif (item >> 5) == 0b110:
                leading_bytes = 1
            elif (item >> 4) == 0b1110:
                leading_bytes = 2
            elif (item >> 3) == 0b11110:
                leading_bytes = 3
            else:
                return False
        else:
            # Check if it's a continuation byte.
            if (item >> 6) != 0b10:
                return False
            leading_bytes -= 1

    # If all leading bytes were correctly followed by continuation bytes
    # return True.
    return leading_bytes == 0
