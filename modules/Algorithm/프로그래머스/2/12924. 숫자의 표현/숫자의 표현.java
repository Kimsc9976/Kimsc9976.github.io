class Solution {
    public int solution(int n) {
        int answer = 0;
        
        int[] array = new int[n+1];
        for (int i = 0; i <= n; i++) {
            array[i] = i;
        }
        
        int a = 1; int b = 1;
        
        while (a <= n & b <= n){
            int target = 0;
            
            for(int j = a; j <=b; j++){
                target += j;
            }
            
            if (target == n){
                answer += 1;
                b += 1;
            }else if(target < n){
                b += 1;
            }else if(target > n){
                a += 1;
            }
            
        }
        
        
        return answer;
    }
}