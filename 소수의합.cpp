#include <vector>
#include <math.h>

using namespace std;

long long solution(int N) {
	long long answer = 0;
	vector<bool> prime(N);



	for (int i = 2; i <= N; i++)
	{
		if (prime[i] == false) {
			answer += i;
			for (int j = i; j <= N; j += i)
				prime[j] = true;
		}
	}


	return answer;
}