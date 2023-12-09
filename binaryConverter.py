def nibble_to_binary(nibble: int) -> str:
    """
    This is a comment
    Input: Nibble (4-bits)
    Output: 4 character binary string
    Example: Input = 10, Output = '1010'
    Example: Input = 8,  Output = '1000'
    """
    return format(nibble, '04b')


def to_binary(number: int) -> str:
    """
    This is a comment
    Input: Number (integer)
    Output: String representing the number in binary prefixed with "0b"
    Example: Input = 255, Output = "0b11111111"
    """
    answer = ""

    # Forever loop
    while True:
        # Integer divide using the // operator
        quotient = number // 2
        # Get the remainder using the % operator
        remainder = number % 2

        # Accumulate result
        answer = nibble_to_binary(remainder) + answer

        # Set the number we need to use for next time
        number = quotient

        # We break the "loop" when division turns to zero
        if (quotient == 0):
            break

    # Remove leading zeros and add '0b' prefix
    answer = answer.lstrip("0") or "0"
    return "0b" + answer


# Test the function
print(to_binary(123456789))
print(to_binary(0b1010101))
print(to_binary(0xDEADBEEF))
