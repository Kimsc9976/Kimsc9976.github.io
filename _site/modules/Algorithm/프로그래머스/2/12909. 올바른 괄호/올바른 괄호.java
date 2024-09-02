import java.util.Stack;

class Solution {
    boolean solution(String s) {
        boolean answer = true;
        
        Stack<Character> stack = new Stack<>();
        
        for(Character c : s.toCharArray()){

            if (stack.size() == 0 & c == ')'){
                stack.add(c); break;
            }else if(c == '('){
                stack.add(c);
            }else if(c == ')'){
                stack.pop();
            }
        }
        
        answer = (stack.size() == 0) ? true : false;

        return answer;
    }
}