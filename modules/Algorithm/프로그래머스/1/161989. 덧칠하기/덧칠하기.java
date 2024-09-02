class Solution {
    public int solution(int n, int m, int[] section) {
        int answer = 1;
        
        int target = section[0];
        for (int place : section){
            if (place - target < m) continue;
            
            target = place;
            answer += 1;
        }
        
        return answer;
    }
}