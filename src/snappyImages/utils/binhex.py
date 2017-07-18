
def hexNibble(nibble):
    hexgits = "0123456789ABCDEF"
    return hexgits[nibble & 0xf]

def hexByte(byte):
    high = hexNibble(byte >> 4)
    return high + hexNibble(byte)

def hexValues3(v1, v2, v3):
    return hexByte(v1) + hexByte(v2) + hexByte(v3)

