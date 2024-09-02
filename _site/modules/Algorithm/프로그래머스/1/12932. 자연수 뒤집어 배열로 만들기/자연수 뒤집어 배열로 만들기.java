class Solution {
    public int[] solution(long n) {
        String numberString = Long.toString(n);
        int length = numberString.length();
        
        int[] answer = new int[length];

        int index = 0; 
        
        while (n != 0){
            int x = (int) (n % 10);
            answer[index] = x;
            n /= 10;
            index++;
        }
        
        return answer;
    }
}