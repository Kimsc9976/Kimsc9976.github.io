#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

#include <stdio.h>

#define _CRT_SECURE_NO_WARNINGS
// 즉 위의 중복되는 변수를 읽어오는 것에 문제가 있을 수 있다,.
using namespace std; // - 이걸 활용해서 네임스페이스를 자동으로 선언함// but 원래의 목적을 상실
// using std::count; 
// using std::endl; // 이렇게 from - import 느낌으로도 사용 가능


int main() {
	int N, K;
	cin >> N >> K;

	vector<int> B;

	int start = 1;
	int end = K;
	int result;
	while (start <= end)
	{
		int sum = 0;
		int mid = (start + end) / 2; // 숫자 Num 은 K 보다 작거나 같다.
		for (int i = 1; i <= N; i++)
		{
			sum += min(N, mid / i);
		}

		if (sum < K) {
			start = mid + 1;
		}
		if (sum >= K) {
			end = mid - 1;
			result = mid;
		}
	}

	cout << result;
	return 0;
}