#include <string>
#include <vector>

using namespace std;

//아이디어: 배열을 순회하며 더 큰값이 있으면 현재위치 배열을 맨 뒤에 추가
//			더 큰 값이 없으면 answer에 1을 더함
//			만약 현재위치가 찾고자 하는 값이면 answer를 반환
int solution(vector<int> priorities, int location) {
	int answer = 0;
	
	//priorities 배열 순회 2중 반복문
	for (int i = 0; i < priorities.size(); i++) {
		for (int j = i; j < priorities.size(); j++) {

			//현재 인덱스보다 더 큰 값이 있으면 현재 배열 값을 배열 뒤에 추가
			if (priorities[i] < priorities[j]) {
				priorities.push_back(priorities[i]);

				//현재 인덱스가 찾고자 하는 위치였다면 인덱스 갱신
				if (i == location)
					location = priorities.size() - 1;

				break;
			}

			//더 큰값이 없다면 answer에 1을 추가하고 
			//찾고자 하는 위치였다면 answer를 반환
			if (j + 1 == priorities.size()) {
				answer++;
				if (i == location)
					return answer;
			}
		}
	}
}