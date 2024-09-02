import java.util.*;

class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        
        int answer = health;
        int continuity = 0;
        int lastTime = attacks[attacks.length - 1][0];
        
        Map<Integer, Integer> attackMap = new HashMap<Integer, Integer>(attacks.length);
        for (int[] attack : attacks){
            int time = attack[0];
            int damage = attack[1];
            attackMap.put(time, damage);
        }

      for (int t = 1; t <= lastTime; t++) {
        Integer attackPower = attackMap.get(t); // Integer로 변경하여 null 가능성을 처리
        if (attackPower != null) { // null 체크
            if (attackPower != 0) { // 숫자가 0이 아닌 경우
                continuity = 0;
                answer = answer - attackPower;

                if (answer <= 0) {
                    answer = -1;
                    break;
                }
            }
        } else {
            continuity++;
            answer = answer + bandage[1];
        }

        if (continuity == bandage[0]) {
            continuity = 0;
            answer = answer + bandage[2];
        }
        answer = (answer > health) ? health : answer;
        // System.out.println(answer);
    }

        
        return answer;
    }
}