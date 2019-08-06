#include <string>
#include <vector>
#include <stack>
#include <iostream>
using namespace std;

vector<int> solution(vector<int> heights) {
	vector<int> answer;
	stack<int> temp;


	//ž ����Ž�� �ݺ���
	for (int i = heights.size() - 1; i > 0; i--) {
		for (int j = i - 1; j >= 0; j--) {
			
			//ž���� ���ؼ� i���� j�� ũ�� jž�� ��ȣ�� ���ÿ� ����
			if (heights[i] < heights[j]) {
				temp.push(j + 1);
				break;
			}

			//������ ���Ҵµ� �� ū ž�� ������ 0�� ���ÿ� ����
			else if (j == 0) {
				temp.push(0);
				break;
			}
		}
	}

	//������ ž�� �񱳴���� �����Ƿ� 0�� ���ÿ� ����
	temp.push(0);

	//���ÿ� ������ top���� ���ʴ�� answer�� ����
	while (!temp.empty()) {
		answer.push_back(temp.top());
		temp.pop();
	}

	return answer;
}
