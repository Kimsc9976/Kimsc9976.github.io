import java.util.*;

class Solution {
    public int solution(int[] ingredient) {
        // 1 빵 2 야채 3 고기 1 빵
        int answer = 0;
        List<Integer> list = new ArrayList<>();
        
        for (int num : ingredient){
            list.add(num);
            
			while(list.size() >= 4) {
				int n = list.size();
				if(!(list.get(n-1) == 1
					&& list.get(n-2)==3
					&& list.get(n-3) ==2
					&& list.get(n-4)==1)) break;
				for(int j=0; j<4; j++) {
					list.remove(list.size() -1);
				}
				answer++;
			}
        }
        
        return answer;
    }
}