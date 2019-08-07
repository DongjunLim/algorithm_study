#include <string>
#include <vector>

using namespace std;

//아이디어: n개의 타일의 경우의 수는 타일의 갯수가 n-2일때의 경우의 수 + n-1일때의 경우의 수 이다.
//          따라서 점화식은 피보나치수열을 이룬다. n = (n-1) + (n-2)
//          이를 DP를 이용한 재귀함수로 구현하였다.

int arr[60001];

int fibo(int N) {
	if (arr[N] != NULL)  return arr[N];

	if (N == 1)            return arr[N] = 1;
	if (N == 2)            return arr[N] = 2;

	arr[N] = (fibo(N - 2) + fibo(N - 1)) % 1000000007;
	return arr[N];


}
int solution(int n) {

	return fibo(n);
}