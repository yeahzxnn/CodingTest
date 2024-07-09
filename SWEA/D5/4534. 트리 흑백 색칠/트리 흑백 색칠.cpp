#include <iostream>
#include <vector>
#define MOD 1000000007

using namespace std;

vector<vector<int>> adj; // 인접 리스트로 트리 표현
vector<vector<long long>> dp; // 각 노드의 DP 값 저장

// DFS를 이용하여 DP 값 계산
void dfs(int node, int parent) {
    dp[node][0] = dp[node][1] = 1; // 초기화: 현재 노드가 흰색 또는 검은색일 때 경우의 수는 최소 1
    
    for (int neighbor : adj[node]) {
        if (neighbor == parent) continue; // 부모 노드는 건너뜀
        dfs(neighbor, node); // 자식 노드에 대해 재귀적으로 DFS 호출
        
        // 현재 노드가 흰색인 경우, 자식 노드는 흰색 또는 검은색이 될 수 있음
        dp[node][0] = dp[node][0] * (dp[neighbor][0] + dp[neighbor][1]) % MOD;
        
        // 현재 노드가 검은색인 경우, 자식 노드는 반드시 흰색이어야 함
        dp[node][1] = dp[node][1] * dp[neighbor][0] % MOD;
    }
}

int main() {
    int T;
    cin >> T; // 테스트 케이스 수 입력
    
    for (int t = 1; t <= T; ++t) {
        int N;
        cin >> N; // 트리의 노드 수 입력
        
        adj.assign(N + 1, vector<int>()); // 인접 리스트 초기화
        dp.assign(N + 1, vector<long long>(2, 0)); // DP 테이블 초기화
        
        for (int i = 0; i < N - 1; ++i) {
            int x, y;
            cin >> x >> y; // 간선 정보 입력
            adj[x].push_back(y); // 인접 리스트에 간선 추가
            adj[y].push_back(x); // 무방향 그래프이므로 양쪽에 추가
        }
        
        dfs(1, -1); // 루트 노드(1번 노드)부터 시작, 부모는 -1로 설정
        
        long long result = (dp[1][0] + dp[1][1]) % MOD; // 루트 노드의 경우의 수 계산
        cout << "#" << t << " " << result << endl; // 결과 출력
    }
    
    return 0;
}
