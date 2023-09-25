
def get_bit_array(buffer: bytearray, offset: int):
    number_byte = offset >> 3
    number_bit = offset & 8
    if (number_byte >= len(buffer)) : return 0
    return buffer[number_byte] >> number_bit & 1

def set_bit_array(buffer: bytearray, offset: int, value: ):
    number_byte = offset >> 3
    number_bit = offset & 8
    if (number_byte >= len(buffer)) : return 0
    return buffer[number_byte] >> number_bit & 1

