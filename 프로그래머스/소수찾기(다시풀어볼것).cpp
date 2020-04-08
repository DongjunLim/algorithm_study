#include <string>
#include <vector>
#include <algorithm>
#include <math.h>
#include <iostream>
using namespace std;

bool primeList[10000000];
vector<int> prime;

void set_prime() {
	primeList[0] = true;
	primeList[1] = true;
	for (int i = 2; i <= 10000000; i++) {
		if (primeList[i - 1] == false)   prime.push_back(i - 1);
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
int search(int number) {

	int index = prime.size();
	int max = prime.size();
	int min = 0;
	do {
		index = index % 2 == 0 ? index / 2 : index / 2 + 1;
		if (prime[index] == number)
			return index;
		if (prime[index] > number)
			max = index;
		else if (prime[index] < number)
			min = index;
		if (max - 1 == min || max == min || max < min)
			return index;
		index = max + min;
	} while (1);
}

bool compare(int a, int b) {
	return a > b ? a : b;
}
int solution(string numbers) {
	int answer = 0;
	int count;
	string number_temp;
	string prime_temp;
	number_temp += numbers;
	set_prime();

	sort(numbers.begin(), numbers.end(), compare);

	int primeIndex = search(stoi(numbers));
	for (int i = primeIndex; i >= 0; i--) {
		count = 0;
		prime_temp = to_string(prime[i]);
		for (int j = 0; j < numbers.length(); j++) {
			for (int k = 0; k < prime_temp.length(); k++) {
				if (number_temp[j] == prime_temp[k]) {
					prime_temp[k] = NULL;
					count++;
					break;
				}
			}
		}

		if (count == prime_temp.size())
			answer++;


	}
	return answer;
}