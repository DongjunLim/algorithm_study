#include <string>
#include <vector>

using namespace std;

string solution(string s) {
	string answer = "";
	int sz = s.length();
	if ((sz % 2) == 0)
	{
		answer.push_back(s[(sz*0.5) - 1]);
		answer.push_back(s[sz*0.5]);
	}
	else
		answer.push_back(s[((sz + 1)*0.5) - 1]);


	return answer;
}