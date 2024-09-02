class Solution {
    public int solution(int n) {
        int answer = 0;
        int[] nums = new int[n+1];
        
        nums[1] = 1;
        
        for (int i = 2; i <=n; i++){
            nums[i] = (int) ((nums[i-1] + nums[i-2]) % 1234567);
        }
        
        return nums[n];
    }
}