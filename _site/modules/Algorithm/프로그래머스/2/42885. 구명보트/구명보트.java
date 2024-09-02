import java.util.Arrays;

class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        
        Arrays.sort(people);
        int count = people.length;
        
        int maxC = count - 1;
        int minC = 0;
        
        while (maxC >= minC){
            if (people[maxC] + people[minC] <= limit){
                minC ++;
            }
            maxC --;
            answer ++;
        }
        
        return answer;
    }
}