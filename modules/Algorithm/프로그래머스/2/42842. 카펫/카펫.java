// 1. 초기 width와 height는 전체 크기를 바탕으로 만들 수 있는 정사각형을 기준으로 생성한다.
// 1-1 이렇게 하게된다면 width * height 는 무조건 brown + yellow 보다 작거나 같다.
// 2. 이때, width는 항상 height 보다 크다
// 4. 따라서, width * height < whole 일 경우, width를 올려준다.
// 3. 그리고 width * height > whole 일 경우, height를 내려준다.
// 5. 그렇게된다면 모든 케이스를 통과할 수 있게된다.

class Solution {
    public int[] solution(int brown, int yellow) {
        int whole = brown + yellow;
        int width = (int)Math.sqrt(whole);
        int height = width;

        while (width * height != whole || (width - 2) * (height - 2) != yellow) {
            if (width * height > whole) {
                height--;
            } else {
                width++;
            }
        }

        return new int[]{width, height};
    }
}


// 투포인터가 일방적인 방식이 아니길래 하라는거 그대로 따라 내려갔다...
class Solution {
    public int[] solution(int brown, int yellow) {
        int whole = brown + yellow;

        for (int width = whole; width >= 3; width--) {
            if (whole % width == 0) { // 세로 길이 계산 가능
                int height = whole / width;
                if ((width - 2) * (height - 2) == yellow) {
                    return new int[]{width, height};
                }
            }
        }
        return new int[]{0, 0}; // 정답을 찾지 못한 경우
    }
}

// 그런데 수식적으로 풀 수 있는 방법이 있더라...! 찾아보길 바란다
