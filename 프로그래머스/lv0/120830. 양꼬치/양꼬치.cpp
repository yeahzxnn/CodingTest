#include <string>
#include <vector>

using namespace std;

int solution(int n, int k) {
    int answer = 0;
    int a = k-n/10;
    
    if(a<=0) k =0;
    else k = a;
    
    answer = n*12000 + k*2000;
    return answer;
}