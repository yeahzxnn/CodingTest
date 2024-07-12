#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// 주어진 순서로 던전을 탐험할 수 있는 최대 던전 수를 계산하는 함수
int calculateMaxDungeons(int k, int** dungeons, size_t dungeons_rows) {
    int count = 0; // 탐험한 던전 수를 저장할 변수
    for (size_t i = 0; i < dungeons_rows; i++) { // 각 던전을 순회하며
        int required = dungeons[i][0]; // 던전 탐험에 필요한 최소 피로도
        int consume = dungeons[i][1]; // 던전을 탐험한 후 소모되는 피로도
        
        if (k >= required) { // 현재 피로도가 최소 필요 피로도 이상인 경우
            k -= consume; // 던전을 탐험하고 피로도를 소모
            count++; // 탐험한 던전 수 증가
        } else {
            break; // 현재 던전을 탐험할 수 없다면 반복문 종료
        }
    }
    return count; // 탐험한 던전 수 반환
}

// 순열을 생성하여 각 순서에 대해 최대 던전 수를 계산하는 함수
void generatePermutations(int k, int** dungeons, size_t dungeons_rows, int start, int* maxDungeons) {
    if (start == dungeons_rows) {
        // 현재 순서에 대해 최대 탐험 가능한 던전 수 계산
        int currentMax = calculateMaxDungeons(k, dungeons, dungeons_rows);
        if (currentMax > *maxDungeons) {
            *maxDungeons = currentMax; // 최대 탐험한 던전 수 갱신
        }
        return;
    }
    
    for (size_t i = start; i < dungeons_rows; i++) {
        // 던전 순서 변경 (순열 생성)
        int* temp = dungeons[start];
        dungeons[start] = dungeons[i];
        dungeons[i] = temp;
        
        // 다음 순서로 진행
        generatePermutations(k, dungeons, dungeons_rows, start + 1, maxDungeons);
        
        // 원래 순서로 복구
        temp = dungeons[start];
        dungeons[start] = dungeons[i];
        dungeons[i] = temp;
    }
}

// solution 함수: 최대 탐험 가능한 던전 수를 계산하는 함수
int solution(int k, int** dungeons, size_t dungeons_rows, size_t dungeons_cols) {
    int maxDungeons = 0; // 최대 탐험한 던전 수를 저장할 변수
    generatePermutations(k, dungeons, dungeons_rows, 0, &maxDungeons); // 순열 생성 및 최대값 갱신
    return maxDungeons; // 최대 탐험한 던전 수 반환
}

int main() {
    int k = 80; // 초기 피로도
    int dungeons_data[3][2] = {{80, 20}, {50, 40}, {30, 10}}; // 던전 리스트 (최소 필요 피로도, 소모 피로도)
    int* dungeons[3] = {dungeons_data[0], dungeons_data[1], dungeons_data[2]};
    
    // 최대 탐험 가능한 던전 수 출력
    printf("%d\n", solution(k, dungeons, 3, 2));
    
    return 0;
}
