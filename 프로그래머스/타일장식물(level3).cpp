#include <string>
#include <vector>
#include <iostream>
using namespace std;


//���̵��: �ѷ��� 4,6,10,16,26,42 �� ������ �Ǻ���ġ ������ �̷�
//          �ʱ� 1,2��° �ε��� ���� 4,6���� �ٲ� ����Լ� ����.
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