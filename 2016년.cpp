#include <string>
#include <vector>

using namespace std;

string solution(int a, int b) {
	string answer = "";
	vector<int> day_count{ 0,31,29,31,30,31,30,31,31,30,31,30,31 };
	vector<string> week{ "THU","FRI","SAT","SUN","MON","TUE","WED" };
	int day = 0;
	for (int i = 0; i < a; i++)
		day += day_count[i];
	day += b;
	answer = week[day % 7];


	return answer;
}