#include <string>
#include <vector>

using namespace std;

//���̵��: n���� Ÿ���� ����� ���� Ÿ���� ������ n-2�϶��� ����� �� + n-1�϶��� ����� �� �̴�.
//          ���� ��ȭ���� �Ǻ���ġ������ �̷��. n = (n-1) + (n-2)
//          �̸� DP�� �̿��� ����Լ��� �����Ͽ���.

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