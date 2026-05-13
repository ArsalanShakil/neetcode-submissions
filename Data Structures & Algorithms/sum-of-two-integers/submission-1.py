class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF        # 32-bit mask
        MAX_INT = 0x7FFFFFFF     # largest positive 32-bit signed int

        while b != 0:
            carry = ((a & b) << 1) & mask
            a = (a ^ b) & mask
            b = carry

        # If a is in the negative range (sign bit set), convert back to Python negative int
        return a if a <= MAX_INT else ~(a ^ mask)
