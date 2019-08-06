#include <string>
#include <vector>
#include <stack>
#include <iostream>
using namespace std;

vector<int> solution(vector<int> heights) {
	vector<int> answer;
	stack<int> temp;


	//탑 완전탐색 반복문
	for (int i = heights.size() - 1; i > 0; i--) {
		for (int j = i - 1; j >= 0; j--) {
			
			//탑끼리 비교해서 i보다 j가 크면 j탑의 번호를 스택에 저장
			if (heights[i] < heights[j]) {
				temp.push(j + 1);
				break;
			}

			//끝까지 돌았는데 더 큰 탑이 없으면 0을 스택에 저장
			else if (j == 0) {
				temp.push(0);
				break;
			}
		}
	}

	//마지막 탑은 비교대상이 없으므로 0을 스택에 저장
	temp.push(0);

	//스택에 정보를 top부터 차례대로 answer에 저장
	while (!temp.empty()) {
		answer.push_back(temp.top());
		temp.pop();
	}

	return answer;
}
