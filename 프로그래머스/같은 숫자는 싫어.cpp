#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> arr)
{
	vector<int> answer;
	int temp = -1;
	int size = arr.size();
	for (int i = 0; i < size; i++) {
		if (temp != arr[i]) {
			temp = arr[i];
			answer.push_back(temp);
		}
	}

	// [����] ��ư�� ������ ��� ���� �� �� �ֽ��ϴ�.
	cout << "Hello Cpp" << endl;

	return answer;
}