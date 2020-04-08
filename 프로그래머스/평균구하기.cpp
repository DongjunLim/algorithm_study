#include <string>
#include <vector>
#include <math.h>

using namespace std;

double solution(vector<int> arr) {
	double answer = 0;
	int temp = 0;
	for (int i = 0; i < arr.size(); i++)
		temp += arr[i];
	answer = (double)temp / (double)arr.size();

	return answer;
}