class Solution {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        
        
        int row_arr1 = arr1.length;
        int col_arr1 = arr1[0].length;
        
        int row_arr2 = arr2.length;
        int col_arr2 = arr2[0].length;
        
        int[][] answer = new int[row_arr1][col_arr2];
        
        for(int i = 0; i < row_arr1; i++){
            for(int j = 0; j < col_arr2; j++){
                for(int k =0; k < col_arr1; k++){
                    answer[i][j] += (arr1[i][k] * arr2[k][j]);
                }
            }
        }
        
        return answer;
    }
}