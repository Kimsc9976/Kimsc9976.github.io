#include <iostream>
#include <algorithm>
#include <string>
#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS
// 즉 위의 중복되는 변수를 읽어오는 것에 문제가 있을 수 있다,.
using namespace std; // - 이걸 활용해서 네임스페이스를 자동으로 선언함// but 원래의 목적을 상실
// using std::count; 
// using std::endl; // 이렇게 from - import 느낌으로도 사용 가능



int main() {
	int N;
	cin >> N;
	int* have = (int*)malloc(N*sizeof(int));

	for (int i = 0; i < N; i++) {
		int num;
		cin >> num;
		have[i] = num;
	}
	sort(have, have + N);

	int M;
	cin >> M;
	int* find = (int*)malloc(M * sizeof(int));
	for (int j = 0; j < M; j++) {
		int num;
		cin >> num;
		int start = 0, end = N-1;

		bool Trigger = false;
		while (start <= end) {
			int mid = (start + end) / 2;
			
			if (num < have[mid]) {
				end = mid - 1;
			}
			else if (num > have[mid]) {
				start = mid + 1;
			}
			else {
				find[j] = 1;
				Trigger = true;
				break;
			}
		}
		if (!Trigger) find[j] = 0;
	}

	for (int a = 0; a < M; a++) {
		cout << find[a] <<' ';
	}
	return 0;
}