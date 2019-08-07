#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

bool desc(int a, int b) {
	return a > b;
}


int solution(vector<vector<int>> triangle) {
	int answer = 0;
	int size = triangle.size();



	for (int i = 1; i < size; i++) {
		for (int j = 0; j < triangle[i].size(); j++) {
			if (j == 0) {
				triangle[i][j] += triangle[i - 1][j];
				continue;
			}
			else if (j == triangle[i].size() - 1) {
				triangle[i][j] += triangle[i - 1][j - 1];
				continue;
			}
			else {
				if (triangle[i - 1][j - 1] >= triangle[i - 1][j])
					triangle[i][j] += triangle[i - 1][j - 1];
				else
					triangle[i][j] += triangle[i - 1][j];
			}
		}
	}
	sort(triangle[size - 1].begin(), triangle[size - 1].end(), desc);

	answer = triangle[size - 1][0];



	return answer;
}