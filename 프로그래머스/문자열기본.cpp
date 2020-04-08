#include <string>
#include <vector>
#include <iostream>
using namespace std;

bool solution(string s) {
	bool answer = true;
	if (!(s.length() == 4 || s.length() == 6))
		answer = false;
	else {
		for (int i = 0; i < s.length(); i++)
		{
			if ((int)s[i] > 64) {
				return false;
			}
		}
	}
	return answer;
}
