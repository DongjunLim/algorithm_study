#include <string>
#include <vector>
#include <queue>
#include <iostream>
using namespace std;


vector<int> solution(vector<int> progresses, vector<int> speeds) {
	vector<int> answer;
	int finish = 100;
	int count = 1;
	int pivot;
	queue<int> temp;
	for (int i = 0; i < progresses.size(); i++)
	{
		if ((finish - progresses[i]) % speeds[i] != 0)
			temp.push(((finish - progresses[i]) / speeds[i]) + 1);
		else
			temp.push(((finish - progresses[i]) / speeds[i]));
	}

	while (!temp.empty()) {
		pivot = temp.front();
		temp.pop();

		while (temp.front() <= pivot && !temp.empty()) {
			temp.pop();
			count++;
		}

		answer.push_back(count);
		count = 1;
	}




	return answer;
}