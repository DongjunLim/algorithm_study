#include <string>
#include <vector>
#include <cmath>
#include <iostream>
using namespace std;

long long solution(int a, int b) {
	long long answer = 0;
	int mx = max(a, b);
	int mn = min(a, b);
	if (a == b)
		return a;
	for (int i = mn; i <= mx; i++) {
		answer += i;
	}
	return answer;
}