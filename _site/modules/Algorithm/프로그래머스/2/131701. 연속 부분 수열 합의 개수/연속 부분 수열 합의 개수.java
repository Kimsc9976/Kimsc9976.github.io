import java.util.HashSet;
import java.util.Set;

class Solution {
    public int solution(int[] elements) {
        int answer = 0;
        int ele_length = elements.length;
        
        Set<Integer> answerSet = new HashSet<>();
        
        for(int i = 0; i < ele_length; i ++){
            int sum = 0;
            for(int j = 0; j < ele_length; j ++){
                sum += elements[(i+j)%ele_length];
                answerSet.add(sum);
            }
        }
        
        
        
        return answerSet.size();
    }
}