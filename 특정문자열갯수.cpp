#include <string>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

bool solution(string s)
{
	bool answer = true;
	int pCount = 0;
	int yCount = 0;
	int size = s.size();
	for (int i = 0; i < size; i++)
	{
		if (s[i] == 'p' || s[i] == 'P')
			pCount++;
		else if (s[i] == 'y' || s[i] == 'Y')
			yCount++;

	}

	if (pCount != yCount)
		answer = false;
	// [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
	cout << "Hello Cpp" << endl;

	return answer;
}