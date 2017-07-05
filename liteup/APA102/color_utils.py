# TODO do I like this?
GAMMA_CORRECT_FACTOR = 2.8


def extract_brightness(r, g, b):
    # These are 12 bits, but we want to shift them to 8
    # we'll use the shift distance to set the brightness val
    # this effectively gives us more value at the bottom
    ## Bitlength is 1- indexed.  1.bit_length() == 1, but it's in the 0th place

    max_bit_length = max(r, g, b).bit_length()

    shift_dist = 0
    if max_bit_length > 8:
        shift_dist = (max_bit_length - 8)

    brightness = (1 << (shift_dist + 1)) - 1

    if shift_dist:
        r = r >> shift_dist
        g = g >> shift_dist
        b = b >> shift_dist

    return (r, g, b, brightness)


def gamma_correct(led_val, num_bits=8):
    max_val = (1 << num_bits) - 1.0
    corrected = pow(led_val / max_val, GAMMA_CORRECT_FACTOR) * max_val
    return int(byte_bound(corrected))


def byte_bound(val):
    """
    make sure value is within 0 - 255
    """
    val = max(0, val)
    val = min(255, val)
    return val


def reverse_gamma_correct(led_val, num_bits=8):
    max_val = (1 << num_bits) - 1.0
    reverse_multiply = led_val / max_val
    reverse_pow = pow(reverse_multiply, 1.0 / GAMMA_CORRECT_FACTOR)
    reverse_div = reverse_pow * max_val
    return int(reverse_div)


def reverse_gamma_color(color, num_bits=8):
    if len(color) == 3:
        r, g, b = color

    elif len(color) == 4:
        r, g, b, brightness = color

    new_r = reverse_gamma_correct(r, num_bits)
    new_g = reverse_gamma_correct(g, num_bits)
    new_b = reverse_gamma_correct(b, num_bits)
    if len(color) == 3:
        return [new_r, new_g, new_b]
    elif len(color) == 4:
        return [new_r, new_g, new_b, brightness]


def gamma_correct_color(color, num_bits=8):
    if len(color) == 3:
        r, g, b = color

    elif len(color) == 4:
        r, g, b, brightness = color

    new_r = gamma_correct(r, num_bits)
    new_g = gamma_correct(g, num_bits)
    new_b = gamma_correct(b, num_bits)
    if len(color) == 3:
        return [new_r, new_g, new_b]
    elif len(color) == 4:
        return [new_r, new_g, new_b, brightness]
