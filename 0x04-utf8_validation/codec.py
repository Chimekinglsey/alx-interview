import codecs

# Encode the number 129 as a UTF-8 byte string
utf8_bytestring = codecs.encode(129, 'utf-8')

# Get the leading byte
leading_byte = utf8_bytestring[0]

# Get the continuation byte
continuation_byte = utf8_bytestring[1]

# Print the leading and continuation bytes
print(f'Leading byte: {leading_byte}')
print(f'Continuation byte: {continuation_byte}')
