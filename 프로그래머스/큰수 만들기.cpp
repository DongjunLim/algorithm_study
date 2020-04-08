#include <string>
#include <vector>
#include <iostream>
using namespace std;

string solution(string number, int k) {
	string answer = "";
	int leng = number.length() - k;
	int idx = 0;
	int count = 0;
	char max;
	while (k > 0 && answer.length() < leng) {

		max = number[idx];
		for (int i = idx; i < idx + k; i++) {
			if (max < number[i + 1]) {
				max = number[i + 1];
				count = i + 1;
			}
		}
		answer.push_back(max);

		k = k - (count - idx);
		idx = count + 1;
		count = idx;

	}
	if (answer.length() < leng) {
		for (int j = idx; j < number.length(); j++)
			answer.push_back(number[j]);
	}

	return answer;
}