#include <string>
#include <vector>
#include <stack>
#include <iostream>
using namespace std;

//아이디어: 스택을 만들고 값이 (면 스택에 푸시,
//           )면 pop을 하고 레이저인지 확인.
//          레이저라면 스택 안에 있는 괄호(스택의 층)를 모두 더해 answer에 저장
//          레이저가 아니면 막대기 길이가 끝난거니 막대기 하나만큼 answer에 더한다.
int solution(string arrangement) {
	int answer = 0;
	int count = 0;
	stack<char> stk;

	//arrangement 배열 전체 순회
	for (int i = 0; i < arrangement.length(); i++) {

		//(는 스택에 추가
		if (arrangement[i] == '(')
			stk.push(arrangement[i]);

		//)면 pop을 하여 쌍을 맞추고 레이저인지 검사
		else {
			stk.pop();

			//레이저라면 레이저 위치에 있는 막대기 갯수만큼 answer에 더한다
			//있는 막대기 갯수: 스택사이즈
			if (arrangement[i - 1] == '(')
				answer += stk.size();

			//레이저가 아니라면 막대길이가 끝난거니 막대 하나만큼을 answer에 더한다.
			else
				answer++;
		}
	}
	return answer;
}