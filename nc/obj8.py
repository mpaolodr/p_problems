"""
Modify the "mystery_string" below until all of the print statements print as expected based on the comments above each print call expression.
"""
mystery_string = "Your task is to discover what this string should be."

# Should print out 48
mystery_string = mystery_string[0:len(mystery_string) - 4]
print(len(mystery_string))

# Should print out 5
mystery_string = "Your task is to discover what this string should be."
mystery_string = mystery_string[3:]
print(mystery_string.index("k"))

# Should print out 4
mystery_string = "cccc"
print(mystery_string.count("c"))

# Should print out "potential"
mystery_string = "Your task potential cover what this string should be."
print(mystery_string[10:19])

# Should print out "sseldrager"
mystery_string = "Your task potential rregardless"
print(mystery_string[30:20:-1])

# Should print out "Ulcigptnil eadeso icmtne"
mystery_string = "U l c i g p t n i l   e a d e s o   i c m t n e"
print(mystery_string[::2])

# Should print out True
mystery_string = "Unloca"
print(mystery_string.startswith("Unlo"))

# Should print out True
mystery_string = "Unlocastance."
print(mystery_string.endswith("stance."))

# Should print out 5
mystery_string = "Your task is to discover"
print(len(mystery_string.split()))
