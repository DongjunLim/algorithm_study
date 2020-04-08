#include <string>
#include <vector>
#include <algorithm>
#include <math.h>
#include <iostream>
using namespace std;

bool primeList[10000000];

void set_prime() {
	primeList[0] = true;
	primeList[1] = true;
	for (int i = 2; i <= 10000000; i++) {
		if (primeList[i] == false) {
			for (int j = 2; j <= sqrt(i); j++) {
				if (i%j == 0 || i == 2) {
					for (int k = i; k < 10000000; k += i)
						primeList[k] = true;
					break;
				}
			}
		}
	}
	return;
}

int solution(string numbers) {

	int answer = 0;
	int n = numbers.length();

	vector<int> temp;
	for (int i = 1; i <= n; i++)
		temp.push_back(i);
	string num;
	string test;
	set_prime();

	cout << endl;

	sort(numbers.begin(), numbers.end());
	for (int i = 0; i < numbers.length(); i++) {
		test = numbers[i];
		if (primeList[atoi(test.c_str())] == false) {

			answer++;
			primeList[atoi(test.c_str())] = true;
		}
	}
	for (int j = n - 1; j >= 1; j--) {
		sort(temp.begin(), temp.end());
		do {
			for (int k = 0; k < temp.size(); k++) {
				if (temp[k] >= 1)   num.push_back(numbers[k]);
			}
			do {
				if (primeList[atoi(num.c_str())] == false) {

					answer++;
					primeList[atoi(num.c_str())] = true;
				}
			} while (next_permutation(num.begin(), num.end()));

			num.clear();
		} while (next_permutation(temp.begin(), temp.end()));
		temp[temp.size() - 1] = -1;

	}
	return answer;
}
