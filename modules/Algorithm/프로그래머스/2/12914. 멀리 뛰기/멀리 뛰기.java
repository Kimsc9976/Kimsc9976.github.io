class Solution {
    public long solution(int n) {
        long answer = 0;
        int[] depth = new int[n+3];
        depth[1] = 1;        
        depth[2] = 2;
        
        for (int i = 3; i < n+1; i++){
            depth[i] = (depth[i-1] + depth[i-2])%1234567;
        }
        
        return depth[n];
    }
}