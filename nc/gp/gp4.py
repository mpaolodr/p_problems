def to_lower_case(string):
    # Your code here

    new_str = ""

    for char in string:

        if ord(char) < 97:

            char = chr(ord(char) + 32)

        new_str += char

    return new_str


def hamming_weight(n):
    # Your code here

    count = 0

    while n > 0:

        n &= n - 1
        count += 1

    return count


print(hamming_weight(0b00000000000000000000001000000011))
print(hamming_weight(0b00000000000000000000000000001000))
print(hamming_weight(0b11111111111111111111111111111011))
