#include <string>
#include <vector>
#include <iostream>
using namespace std;


//아이디어: 둘레가 4,6,10,16,26,42 로 변형된 피보나치 수열을 이룸
//          초기 1,2번째 인덱스 값만 4,6으로 바꿔 재귀함수 적용.
long long arr[81];

long long fibo(int n) {
	if (arr[n] != NULL) return arr[n];

	if (n == 1)         return arr[n] = 4;

	else if (n == 2)    return arr[n] = 6;

	else             return arr[n] = fibo(n - 2) + fibo(n - 1);
}

long long solution(int N) {
	return fibo(N);

}