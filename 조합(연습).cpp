#include <iostream>
#include <vector>
#include <string>
using namespace std;

int c(int n, int k) {
	if (k == 0 || n == k)	return 1;
	return c(n - 1, k - 1) + c(n - 1, k);

}

int main()
{
	int num = c(10, 3);
	cout << "result: " << num;
	return 0;

}