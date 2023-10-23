def validUTF8(data):
    leading_bytes = 0

    for item in data:
        # Check if the most significant bit is 0 or if it's the start of a multi-byte character.
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

    # If all leading bytes were correctly followed by continuation bytes, return True.
    return leading_bytes == 0
