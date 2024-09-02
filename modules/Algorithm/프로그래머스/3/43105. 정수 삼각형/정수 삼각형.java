public class Solution {
    public int solution(int[][] triangle) {
        for (int i = triangle.length - 2; i >= 0; i--) {
            for (int j = 0; j <= i; j++) {
                triangle[i][j] += Math.max(triangle[i + 1][j], triangle[i + 1][j + 1]);
            }
        }
        return triangle[0][0];
    }
}
// class Solution {
    
    
//     private static int dfs(int row, int col,int sum, 
//                            int triangleRow, int[][] triangle)
//     {
//         if (row == triangleRow) return sum;
        
//         sum += triangle[row][col];
        
//         int left = dfs(row + 1, col, sum, triangleRow, triangle);
//         int right = dfs(row + 1, col + 1, sum, triangleRow, triangle);
        
//         sum = Math.max(sum, left);
//         sum = Math.max(sum, right);
        
//         return sum;
//     }
    
//     public int solution(int[][] triangle) {
//         int answer = 0;
//         int n = triangle.length;
                
//         return dfs(0, 0, 0, n, triangle);
//     }
// }