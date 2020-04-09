#include <iostream>
#include <stack>
#include <string>
using namespace std;

int arr[102][102];
int check[102][102];
int answer;

int main(int argc, char **argv)
{
    int test_case;
    int T = 10;
    int N;
    stack<int> route;

    for(int tc = 1; tc<11; tc++){
        cin >> N;
        memset(arr, -1, sizeof(arr));
        string s;
 
        int x = 0;
        int y = 0;
 
        for (int i = 1; i < 101; i++) {
            cin >> s;
            for (int j = 1; j < 101; j++) {
                arr[i][j] = s[j - 1] - '0';
                if (arr[i][j] == 2) {
                    y = i;
                    x = j;
                }
            }
        }




        
        if (answer == 1)
            cout << "#" << tc << " 1" << endl;
        else 
            cout << "#" << tc << " 0" << endl;
 
        answer = 0;
        memset(check, 0, sizeof(check));
    

    }

    return 0;
}