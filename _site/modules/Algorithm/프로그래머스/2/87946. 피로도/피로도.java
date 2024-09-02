import java.util.Arrays;

class Solution {
    
    private int DFS(int k, boolean[] isTravel, int[][] dungeons, int cnt){
        int result = cnt;

        for(int i = 0; i < dungeons.length; i++){
            int minFatigue = dungeons[i][0];
            int usageFatigue = dungeons[i][1];
            
            if (minFatigue <= k && !isTravel[i]){
                isTravel[i] = true;
                result = Math.max(result, DFS(k - usageFatigue, isTravel, dungeons, cnt + 1));
                isTravel[i] = false;
            }
        }
        
        return result;
    }
    
    public int solution(int k, int[][] dungeons) {
        boolean[] isTraveled = new boolean[dungeons.length];
        return DFS(k, isTraveled, dungeons, 0);
    }
}