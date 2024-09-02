class Solution {
    public double solution(int[] arr) {
        double answer = 0;
        
        for(int num : arr){
            answer = (double) answer + num;
        }
        
        
        return answer/arr.length;
    }
}