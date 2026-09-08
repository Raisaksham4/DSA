class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        num = 0
        while x > 0:
            digit = x % 10
            num = num * 10 + digit
            x //= 10
        num *= sign
        if num < -(2**31) or num > 2**31 - 1:
            return 0

        return num
        