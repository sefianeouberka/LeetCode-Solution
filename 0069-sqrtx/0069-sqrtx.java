class Solution {
    public int mySqrt(int x) {
        if (x < 2) {
            return x;
        }
        
        long limit = x / 2;
        for (long i = 0; i <= limit+1; i++) {
            if (i * i == x) {
                return (int) i;
            } 
            else if ((i - 1) * (i - 1) < x && x < i * i) {
                return (int) (i - 1);
            }
        }
        return 0;
    }
}