import java.util.HashSet;
import java.util.Queue;
import java.util.LinkedList;
import java.util.List;

class Solution {
    int maxDepth = 0;
    public class Pair<U, V>{
        public final U node;
        public final V depth;
        
        public Pair(U node, V depth){
            this.node = node;
            this.depth = depth;
        }
        
    }
    
    public int solution(int n, int[][] edge) {
        int answer = 0;
        
        int[] isVisited = new int[n+1];
        isVisited[1] = 1;
        HashSet<Integer>[] Tree = new HashSet[n+1];
        
        for (int i = 0; i < Tree.length; i++) {
            Tree[i] = new HashSet<Integer>();
        }
        
        for (int[] node : edge){
            Tree[node[0]].add(node[1]);
            Tree[node[1]].add(node[0]);
        }
        
        Queue<Pair<Integer, Integer>> queue =  new LinkedList();
        
        queue.add(new Pair(1, 1));
        
        while (!queue.isEmpty()){
            Pair<Integer, Integer> now = queue.poll();
            maxDepth = (maxDepth < now.depth) ? now.depth : maxDepth;
            
            for(int item : Tree[now.node]){
                if (isVisited[item] != 0) continue;
                

                isVisited[item] = now.depth+1;
                queue.add(new Pair(item, now.depth+1));
            }
        }
        
        // System.out.println(maxDepth);
        for(int i = 1; i <= n; i ++){
            // System.out.println(isVisited[i]);
            if (isVisited[i] == maxDepth){
                answer ++;
            }
        }
        
        return answer;
    }
}