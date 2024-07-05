#include <iostream>
#include <deque>

using namespace std;

deque<int> dq; // 덱을 이용하여 큐와 스택의 동작을 구현
int n, m; // n: 자료구조의 수, m: 수열의 길이
bool flag[100001]; // 자료구조의 타입을 저장하는 배열, 0: queue, 1: stack

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin >> n; // 자료구조의 수 입력
    for(int i = 0; i < n; i++){
        cin >> flag[i]; // 각 자료구조의 타입 입력
    }
    
    for(int i = 0; i < n; i++){
        int x;
        cin >> x; // 각 자료구조의 초기 원소 값 입력
        if(flag[i] == 0) // 자료구조가 큐일 때만 덱에 원소 삽입
            dq.push_back(x);
    }
    
    cin >> m; // 수열의 길이 입력
    for(int i = 0; i < m; i++){
        int y;
        cin >> y; // 수열의 각 원소 입력
        dq.push_front(y); // 덱의 앞에 새 원소 삽입
        cout << dq.back() << " "; // 덱의 뒤에서 원소를 출력
        dq.pop_back(); // 덱의 뒤에서 원소 제거
    }
    
    // 모든 자료구조가 스택일 경우에는 dq를 사용하지 않음
    // 수열의 각 원소에 대해 새 덱에 push_front 후 pop_back 과정 반복
    
    return 0;
}
