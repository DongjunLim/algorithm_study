#include <string>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> solution(vector<int> answers) {
	vector<int> answer;
	int answers_size = answers.size();
	vector<int> first{ 1,2,3,4,5,0 };
	vector<int> second{ 2,1,2,3,2,4,2,5,0 };
	vector<int> third{ 3,3,1,1,2,2,4,4,5,5,0 };

	for (int i = 0; i < answers_size; i++) {
		if (answers[i] == first[i % 5])
			first[5]++;

		if (answers[i] == second[i % 8])
			second[8]++;

		if (answers[i] == third[i % 10])
			third[10]++;
	}
	if (first[5] >= second[8] && first[5] >= third[10])
		answer.push_back(1);
	if (second[8] >= first[5] && second[8] >= third[10])
		answer.push_back(2);
	if (third[10] >= first[5] && third[10] >= second[8])
		answer.push_back(3);



	return answer;
}