class Solution {
    public int solution(int n) {
        int cnt = Integer.bitCount(n);
        int answer = n;

        while (Integer.bitCount(++answer) != cnt) {}

        return answer;
    }
}