class Solution:
    def mySqrt(self, x: int) -> int:
        num = x/2
        for i in range(0, int(num + 2 )) :
            if i*i == x :
                return i
            elif (i-1)*(i-1) < x < i*i :
                return i-1


