class Solution {
    public String solution(String s) {
        String answer = "";

        String[] words = s.toLowerCase().split("");
        Boolean flag = true;
            
        for(String word : words){
            answer += (flag) ? word.toUpperCase() : word;
            flag = (word.equals(" ")) ? true : false;
        }
        
        return answer;
    }
}
// 왜 계속 실패했습니다가 나오나 했었는데, " " 공백이 중복으로 나오는걸 고려를 안했어서
String[] words = s.toLowerCase().split(" "); // 이런식으로 작업을 했던게 문제가 되었었다.


// 아래는 그 전에 정 안되겠어서 스트링 빌더를 활용해 만들었던 것 
-- 효율은 이게 더 좋게나옴, 
    1. Character로 탐색을 하는 것으로 인한 한번만 순회하는 것, 
    2. split으로 분리하지 않으므로 메모리소모 및 추가작업을 안하는 것
    이 두가지가 크다고 생각함
class Solution {
    public String solution(String s) {
        StringBuilder answer = new StringBuilder();

        // 첫 글자를 대문자로 시작하기 위해 'true'로 설정
        boolean isNewWord = true;

        for (char ch : s.toCharArray()) {
            if (ch == ' ') {
                isNewWord = true;
                answer.append(ch);
            } else {
                if (isNewWord) {
                    answer.append(Character.toUpperCase(ch));
                    isNewWord = false;
                } else {
                    answer.append(Character.toLowerCase(ch));
                }
            }
        }

        return answer.toString();
    }
}
