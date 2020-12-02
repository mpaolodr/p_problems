def evenDigitsOnly(n):

    nums = [1 for char in str(n) if int(char) % 2 != 0]

    return len(nums) == 0
