class Solution {
    public int solution(int n) {
        int answer = 0;
        int target = (int) Math.sqrt(n);
        
        for (int i = 1; i <= target; i ++){
            if ( n % i == 0){
                answer += i;
                if (n/i == i) continue;
                answer += n/i;
            }
        }
        
        return answer;
    }
}