#include <string>
#include <vector>
#include <stack>
#include <iostream>
using namespace std;

//���̵��: ������ ����� ���� (�� ���ÿ� Ǫ��,
//           )�� pop�� �ϰ� ���������� Ȯ��.
//          ��������� ���� �ȿ� �ִ� ��ȣ(������ ��)�� ��� ���� answer�� ����
//          �������� �ƴϸ� ����� ���̰� �����Ŵ� ����� �ϳ���ŭ answer�� ���Ѵ�.
int solution(string arrangement) {
	int answer = 0;
	int count = 0;
	stack<char> stk;

	//arrangement �迭 ��ü ��ȸ
	for (int i = 0; i < arrangement.length(); i++) {

		//(�� ���ÿ� �߰�
		if (arrangement[i] == '(')
			stk.push(arrangement[i]);

		//)�� pop�� �Ͽ� ���� ���߰� ���������� �˻�
		else {
			stk.pop();

			//��������� ������ ��ġ�� �ִ� ����� ������ŭ answer�� ���Ѵ�
			//�ִ� ����� ����: ���û�����
			if (arrangement[i - 1] == '(')
				answer += stk.size();

			//�������� �ƴ϶�� ������̰� �����Ŵ� ���� �ϳ���ŭ�� answer�� ���Ѵ�.
			else
				answer++;
		}
	}
	return answer;
}