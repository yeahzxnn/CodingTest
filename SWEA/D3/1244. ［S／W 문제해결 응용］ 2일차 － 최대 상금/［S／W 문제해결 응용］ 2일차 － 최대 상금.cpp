#include <iostream>
#include <unordered_map>
#include <algorithm>

using namespace std;

string max_number;
unordered_map<string, bool> visited;

void find_max(string num, int swaps) {
    if (swaps == 0) {
        if (num > max_number) {
            max_number = num;
        }
        return;
    }

    string original_num = num;
    if (visited[original_num + to_string(swaps)]) {
        return;
    }
    visited[original_num + to_string(swaps)] = true;

    int len = num.length();
    for (int i = 0; i < len - 1; ++i) {
        for (int j = i + 1; j < len; ++j) {
            swap(num[i], num[j]);
            find_max(num, swaps - 1);
            swap(num[i], num[j]);
        }
    }
}

int main() {
    int T;
    cin >> T;
    
    for (int t = 1; t <= T; ++t) {
        string num;
        int max_swaps;
        cin >> num >> max_swaps;
        
        max_number = "0";
        visited.clear();
        find_max(num, max_swaps);
        
        cout << "#" << t << " " << max_number << endl;
    }
    
    return 0;
}
