#include <iostream>

using namespace std; // - 이걸 활용해서 네임스페이스를 자동으로 선언함// but 원래의 목적을 상실
// using std::count; 
// using std::endl; // 이렇게 from - import 느낌으로도 사용 가능

int main(){
  int N = 0;
  cin >> N;
  int ans = 0;
  int length = 10;
  int paper[101][101] = {0,};
  for (int i = 0; i < N; i++)
  {
    int x;
    int y;
    cin >> x >> y ;
    for (int a = x; a<x+10; a++)
    {
      for(int b = y; b<y+10;b++)
      {
        paper[a][b] = 1;
      }
    }
  }

  for (int a = 1; a<101; a++)
  {
    for(int b = 1; b<101;b++)
    {
      if( paper[a][b] == 1 )
      {
        ans ++;
      }
    }
  }
  cout << ans << endl;

  return 0;
}