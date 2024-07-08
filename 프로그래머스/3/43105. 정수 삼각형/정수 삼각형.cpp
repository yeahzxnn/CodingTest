#include <string>
#include <vector>
using namespace std;

int solution(vector<vector<int>> triangle) {
    int n = triangle.size();
    
    // 맨 아래 행부터 시작하여 위로 올라감
    for (int i = n - 2; i >= 0; --i) {
        for (int j = 0; j <= i; ++j) {
            // 아래 행의 왼쪽 및 오른쪽 요소 중 큰 값을 현재 요소에 더함
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1]);
        }
    }
    
    // 최종적으로 꼭대기의 값이 최대 경로 합이 됨
    return triangle[0][0];
}