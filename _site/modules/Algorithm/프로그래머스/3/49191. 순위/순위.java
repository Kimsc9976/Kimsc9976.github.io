import java.util.*;
 
class Solution {
   
    public int solution(int n, int[][] results) {
        int answer = 0;
        int[][] matrix = new int[n+1][n+1];
        
        for(int i = 0; i < results.length; i++){
            int A = results[i][0];
            int B = results[i][1];

            matrix[A][B] = 1; 
            matrix[B][A] = -1; 
        }
        
        // a와 b와의 전적, b와 c와의 전적을 비교해서 실력차를 알아본다.
        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= n; j++){
                for(int k = 1; k <= n; k++){
                    if(matrix[i][k] == 1 && matrix[k][j] == 1){
                        matrix[i][j] = 1;
                        matrix[j][i] = -1;
                    }
                    if(matrix[i][k] == -1 && matrix[k][j] == -1){
                        matrix[i][j] = -1;
                        matrix[j][i] = 1;
                    }
                }
            }
        }
        
        for(int i = 1; i <= n; i++){
            int cnt = 0; 
            for(int j = 1; j <= n; j++){
                if(matrix[i][j] != 0) cnt++;
            }
            if(cnt == n-1) answer++;
        }
        
        return answer;
        
    }
}
