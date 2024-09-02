#include <iostream>
#include <queue>
#include <tuple>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

char matrix[1000][1000];
bool is_travel[1000][1000][10] = { false, };
int result = 2001;

int dx[] = {1, -1, 0, 0};
int dy[] = {0, 0, 1, -1};
int bfs(int n, int m, int k) {
	queue<tuple<int, int, int, int>> que;
	que.push(make_tuple(1, 0, 0, 0));

	while (!que.empty()) {
		tuple<int, int, int, int> now = que.front();
		que.pop();

		int depth = get<0>(now);
		int x = get<1>(now);
		int y = get<2>(now);
		int z = get<3>(now);
		if (x == n-1 && y == m-1)
		{
			return depth;
		}

		for (int d = 0; d < 4; d++) {
			int nx = x + dx[d];
			int ny = y + dy[d];
			int nz = z;

			if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
			if (is_travel[nx][ny][nz]) continue;
			if (matrix[nx][ny] == '1' && nz >= k) continue;
			//cout << nx<<ny <<" "<<matrix[nx][ny] << "depth : "<< depth<<endl;
			if (matrix[nx][ny] == '1') {
				nz = z + 1;
			}
			is_travel[nx][ny][nz] = true;
			tuple<int, int, int, int> next = { depth+1, nx, ny, nz };
			que.push(next);
		}
	}

	return 2001;
}
int main() {

	int N, M, K;
	cin >> N >> M >> K;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			char num;
			cin >> num;
			matrix[i][j] = num;
		}
	}
	int rlt = bfs(N,M,K);
	result = (rlt != 2001)? rlt : -1;
	cout << result << endl;
	return 0;
}