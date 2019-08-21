#include <string>
#include <vector>
#include <iostream>
using namespace std;




int solution(int n, vector<int> lost, vector<int> reserve) {
	int answer = 0;
	int j = 0;
	bool sw;
	answer = n - lost.size();
	int temp;
	for (int i = 0; i < lost.size(); i++) {
		for (int j = 0; j < reserve.size(); j++) {
			if (lost[i] == reserve[j]) {
				answer++;
				reserve[j] = -1;
				lost[i] = -3;
				cout << answer << endl;
				break;
			}
		}
	}
	for (int i = 0; i < lost.size(); i++) {
		for (int j = 0; j < reserve.size(); j++) {
			if (lost[i] == reserve[j] - 1 || lost[i] == reserve[j] + 1) {
				answer++;
				reserve[j] = -1;
				break;
			}
		}
	}

	return answer;
}