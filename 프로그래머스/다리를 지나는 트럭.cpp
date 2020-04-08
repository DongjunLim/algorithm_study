#include <string>
#include <vector>
#include <queue>
#include <iostream>
using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
	int answer = 0;
	int time = 0;		//�ð���
	int idx = 0;		//truck_weights �迭�� Ž���� �ε�������
	int capa = weight;	//���� Ʈ���� ������ �� �ִ� �����߷�
	
	queue<pair<int, int>> bridge;		//�ٸ� ���� �ִ� Ʈ���� ���Կ� ���Խð��� ������ ť

	//����ϴ� Ʈ���� �ٸ��� �ǳʴ� Ʈ���� ���������� �ݺ�
	while (!bridge.empty() || idx < truck_weights.size()) {
		time++;

		//�ٸ��� �ǳ� Ʈ���� �ִ��� Ȯ��
		if (time - bridge.front().second >= bridge_length) {
			capa += bridge.front().first;
			bridge.pop();
		}

		//������ �� �ִ� Ʈ���� �ִ��� Ȯ��
		if (capa >= truck_weights[idx] && idx < truck_weights.size()) {
			bridge.push(pair<int, int>(truck_weights[idx], time));
			capa -= truck_weights[idx];
			idx++;
		}
	}

	answer = time;
	return answer;
}

