class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2 : return n
        f_2 = 2
        f_1 = 1
        for i in range(3, n+1) :
            current = f_1 + f_2
            f_1 = f_2
            f_2 = current
        return f_2
