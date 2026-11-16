class Solution {
    public int climbStairs(int n) {
        if(n <= 2) {
            return n;
        }
        int f_1 = 1;
        int f_2 = 2;

        for(int i = 3; i < n + 1; i++){
            int current = f_1+f_2;
            f_1 = f_2;
            f_2 = current;
        }
        return f_2;
    }
}