#include<iostream>
#include<queue>
#include<string>
#include<tuple>
 
#define endl "\n"
#define MAX 1000
#define INF 987654321
using namespace std;
 
int N, M, K;
int MAP[MAX][MAX];
bool Visit[MAX][MAX][11];
 
int dx[] = { 0, 0, 1, -1 };
int dy[] = { 1, -1, 0, 0 };
 
void Input()
{
    cin >> N >> M >> K;
    for (int i = 0; i < N; i++)
    {
        string Inp; cin >> Inp;
        for (int j = 0; j < Inp.length(); j++)
        {
            MAP[i][j] = Inp[j] - '0';
            /*for (int k = 0; k < 11; k++)
            {
                Visit[i][j][k] = INF;
            }*/
        }
    }
}
 
void BFS(int a, int b)
{
    queue<pair<tuple<int, int, int>, pair<int, string>>> Q;
    Q.push(make_pair(make_tuple(a, b, 1), make_pair(0, "Morning")));
    Visit[a][b][0] = true;
 
    while (Q.empty() == 0)
    {
        int x = get<0>(Q.front().first);
        int y = get<1>(Q.front().first);
        int Cnt = get<2>(Q.front().first);
        int K_Num = Q.front().second.first;
        string Day = Q.front().second.second;
        Q.pop();
 
        if (x == N - 1 && y == M - 1)
        {
            cout << Cnt << endl;
            return;
        }
 
        for (int i = 0; i < 4; i++)
        {
            int nx = x + dx[i];
            int ny = y + dy[i];
 
            if (nx >= 0 && ny >= 0 && nx < N && ny < M)
            {
                if (MAP[nx][ny] == 0)
                {
                    if (Visit[nx][ny][K_Num] == false)
                    {
                        Visit[nx][ny][K_Num] = true;
                        if (Day == "Morning") Q.push(make_pair(make_tuple(nx, ny, Cnt + 1), make_pair(K_Num, "Night")));
                        else Q.push(make_pair(make_tuple(nx, ny, Cnt + 1), make_pair(K_Num, "Morning")));
                    }
                }
                else if (MAP[nx][ny] == 1)
                {
                    if (K_Num < K)
                    {
                        if (Visit[nx][ny][K_Num + 1] == false)
                        {
                            if (Day == "Morning")
                            {
                                Visit[nx][ny][K_Num + 1] = true;
                                Q.push(make_pair(make_tuple(nx, ny, Cnt + 1), make_pair(K_Num + 1, "Night")));
                                
                            }
                            else
                            {
                                Q.push(make_pair(make_tuple(x, y, Cnt + 1), make_pair(K_Num, "Morning")));
                            }
                        }                        
                    }
                }
            }
        }
    }
    cout << -1 << endl;
    return;
}
 
void Solution()
{
    BFS(0, 0);
}
 
void Solve()
{
    Input();
    Solution();
}
 
int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
 
    //freopen("Input.txt", "r", stdin);
    Solve();
 
    return 0;
}
 
