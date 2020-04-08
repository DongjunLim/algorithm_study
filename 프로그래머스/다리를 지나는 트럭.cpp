#include <string>
#include <vector>
#include <queue>
#include <iostream>
using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
	int answer = 0;
	int time = 0;		//시간초
	int idx = 0;		//truck_weights 배열을 탐색할 인덱스변수
	int capa = weight;	//현재 트럭을 수용할 수 있는 가용중량
	
	queue<pair<int, int>> bridge;		//다리 위에 있는 트럭의 무게와 진입시간을 저장할 큐

	//대기하는 트럭과 다리를 건너는 트럭이 없을때까지 반복
	while (!bridge.empty() || idx < truck_weights.size()) {
		time++;

		//다리를 건넌 트럭이 있는지 확인
		if (time - bridge.front().second >= bridge_length) {
			capa += bridge.front().first;
			bridge.pop();
		}

		//진입할 수 있는 트럭이 있는지 확인
		if (capa >= truck_weights[idx] && idx < truck_weights.size()) {
			bridge.push(pair<int, int>(truck_weights[idx], time));
			capa -= truck_weights[idx];
			idx++;
		}
	}

	answer = time;
	return answer;
}

