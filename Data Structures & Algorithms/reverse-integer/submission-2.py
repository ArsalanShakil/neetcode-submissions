class Solution:
    def reverse(self, x: int) -> int:
        MIN, MAX = -2147483648, 2147483647
        res = 0
        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)
            # Check overflow using truncated division (matches C semantics)
            if res > MAX // 10 or (res == MAX // 10 and digit > 7):
                return 0
            if res < -(-MIN // 10) or (res == -(-MIN // 10) and digit < -8):
                return 0
            res = res * 10 + digit
        return res