#include <iostream>
using namespace std;

int main() {
    int a1, a0;
    int c, n0;

    // 첫째 줄에서 함수 f(n)의 계수 a1과 a0를 입력받음
    cin >> a1 >> a0;
    
    // 둘째 줄에서 양의 정수 c를 입력받음
    cin >> c;

    // 셋째 줄에서 양의 정수 n0를 입력받음
    cin >> n0;

    // 모든 n >= n0에 대하여 f(n) <= c * n이 성립하는지 검사
    // 여기서 중요한 점은 n이 n0 이상의 모든 수에 대해 성립해야 한다는 점.
    bool isBigO = true; // 초기 상태를 true로 설정

    for (int n = n0; n <= 100; ++n) {
        if (a1 * n + a0 > c * n) {
            isBigO = false; // 조건을 만족하지 않는 경우
            break;
        }
    }

    // 결과 출력 (조건을 만족하면 1, 만족하지 않으면 0)
    if (isBigO) {
        cout << 1 << endl;
    } else {
        cout << 0 << endl;
    }

    return 0;
}
