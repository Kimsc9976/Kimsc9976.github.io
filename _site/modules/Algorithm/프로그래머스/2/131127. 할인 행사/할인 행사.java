import java.util.HashMap;
import java.util.Map;

class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        Map<String, Integer> wantMap = new HashMap<>();
        for (int i = 0; i < want.length; i++) {
            wantMap.put(want[i], number[i]);
        }

        int answer = 0;
        for (int i = 0; i <= discount.length - 10; i++) {
            Map<String, Integer> currentWindow = new HashMap<>();
            for (int j = i; j < i + 10; j++) {
                currentWindow.put(discount[j], currentWindow.getOrDefault(discount[j], 0) + 1);
            }
            if (matches(wantMap, currentWindow)) {
                answer++;
            }
        }

        return answer;
    }

    private boolean matches(Map<String, Integer> wantMap, Map<String, Integer> currentWindow) {
        for (String key : wantMap.keySet()) {
            if (currentWindow.getOrDefault(key, 0) < wantMap.get(key)) {
                return false;
            }
        }
        return true;
    }
}
