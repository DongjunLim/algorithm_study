#include <string>
#include <vector>
#include <stack>
#include <iostream>
using namespace std;

vector<int> solution(vector<int> heights) {
	vector<int> answer;
	stack<int> temp;

	for (int i = heights.size() - 1; i > 0; i--) {
		for (int j = i - 1; j >= 0; j--) {
			if (heights[i] < heights[j]) {
				temp.push(j + 1);
				break;
			}
			else if (j == 0) {
				temp.push(0);
				break;
			}
		}
	}
	temp.push(0);
	while (!temp.empty()) {
		answer.push_back(temp.top());
		temp.pop();
	}

	return answer;
}
