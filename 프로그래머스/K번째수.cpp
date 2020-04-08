#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
	vector<int> answer;
	vector<int> result;
	int cSize = commands.size();
	for (int i = 0; i < cSize; i++) {
		result.resize(0);

		for (int j = commands[i][0] - 1; j < commands[i][1]; j++) {
			result.push_back(array[j]);
		}
		sort(result.begin(), result.end());
		answer.push_back(result[commands[i][2] - 1]);
	}

	return answer;
}