#include <string>
#include <vector>
#include <math.h>
using namespace std;

bool isPrime(int n)
{
	static vector<int> primes{ 2,3,5,7 };
	int rootNumber;
	int i, j = 0;
	if (n == 1)
		return false;
	if (n == 2) {
		primes.push_back(n);
		return true;
	}
	if (n % 2 == 0)
		return false;
	rootNumber = sqrt(n);
	while (i <= rootNumber) {
		i = primes[j++];
		if (n%i == 0)
			return false;

	}
	for (; i <= rootNumber; i += 2)
	{
		if (n%i == 0)
			return false;
	}
	primes.push_back(n);
	return true;

}

int solution(int n) {
	int answer = 0;
	vector<bool> seive(n + 1);
	for (int i = 2; i <= n; i++) {
		if (seive[i] == false)
		{
			answer++;
		}
		for (int j = i; j <= n; j += i)
		{
			seive[j] = true;
		}
	}
	return answer;

}