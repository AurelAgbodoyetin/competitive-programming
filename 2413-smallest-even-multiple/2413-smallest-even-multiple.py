class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        p = n
        while(p % 2 != 0):
            p = p + n
        return p
        