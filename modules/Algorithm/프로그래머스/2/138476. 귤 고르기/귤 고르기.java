import java.util.*;

class Solution {
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        Map<Integer, Integer> tangerineCount = new HashMap<>();

        for (int size : tangerine) {
            tangerineCount.put(size, tangerineCount.getOrDefault(size, 0) + 1);
        }
        
        List<Map.Entry<Integer, Integer>> list = new ArrayList<>(tangerineCount.entrySet());
        list.sort((o1, o2) -> o2.getValue().compareTo(o1.getValue()));
        
        // // 결과 출력
        // for (Map.Entry<Integer, Integer> entry : list) {
        //     System.out.println("Size: " + entry.getKey() + ", Count: " + entry.getValue());
        // }
        
        int count = 0;
        while (count < k){
            count += list.get(answer).getValue();
            answer ++;
        }
        
        return answer;
    }
}