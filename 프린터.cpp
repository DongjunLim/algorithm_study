#include <string>
#include <vector>

using namespace std;

//���̵��: �迭�� ��ȸ�ϸ� �� ū���� ������ ������ġ �迭�� �� �ڿ� �߰�
//			�� ū ���� ������ answer�� 1�� ����
//			���� ������ġ�� ã���� �ϴ� ���̸� answer�� ��ȯ
int solution(vector<int> priorities, int location) {
	int answer = 0;
	
	//priorities �迭 ��ȸ 2�� �ݺ���
	for (int i = 0; i < priorities.size(); i++) {
		for (int j = i; j < priorities.size(); j++) {

			//���� �ε������� �� ū ���� ������ ���� �迭 ���� �迭 �ڿ� �߰�
			if (priorities[i] < priorities[j]) {
				priorities.push_back(priorities[i]);

				//���� �ε����� ã���� �ϴ� ��ġ���ٸ� �ε��� ����
				if (i == location)
					location = priorities.size() - 1;

				break;
			}

			//�� ū���� ���ٸ� answer�� 1�� �߰��ϰ� 
			//ã���� �ϴ� ��ġ���ٸ� answer�� ��ȯ
			if (j + 1 == priorities.size()) {
				answer++;
				if (i == location)
					return answer;
			}
		}
	}
}