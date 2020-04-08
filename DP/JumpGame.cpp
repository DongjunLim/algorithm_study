#include <iostream>
#include <vector>
#include <math.h>
using namespace std;

vector<vector<bool>> memo(20, vector<bool>(20, false));

int maze[7][7] = {
    {2, 5, 1, 6, 1, 4, 1},
    {6, 1, 1, 2, 2, 9, 3},
    {7, 2, 3, 2, 1, 3, 1},
    {2, 1, 3, 1, 7, 1, 2},
    {5, 1, 2, 3, 4, 1, 2},
    {4, 3, 1, 2, 3, 4, 1},
    {2, 5, 2, 9, 4, 3, 0},
};

bool solution()
{

    int end = 6;
    int start = 0;
    int x = end, y = end - 1;
    memo[end][end] = true;

    
    while (x >= 0)
    {
        while (y >= 0)
        {
            if (memo[x + maze[x][y]][y] == true)
            {
                memo[x][y] = true;
            }
            if (memo[x][y + maze[x][y]] == true)
            {
                memo[x][y] = true;
            }
            y--;
        }
        y = end;
        x--;
    }

    return memo[start][start];
}

int main()
{
    cout << solution() << endl;
    return 0;
}
