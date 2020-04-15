#include <stdio.h>
#include <iostream>
#define MAX 50
using namespace std;

struct Node
{
    char data;
    Node *preNode;
};

struct Stack
{
    Node *top;
};

void initStack(Stack *s)
{
    s->top = NULL;
}

bool isEmpty(Stack *s)
{
    return s->top ? false : true;
}

void pushBack(Stack *s, int data)
{
    Node newNode;
    newNode.data = data;
    newNode.preNode = s->top;

    s->top = &newNode;
    return;
}

bool pop(Stack *s)
{
    if (isEmpty(s))
    {
        return false;
    }
    int temp = s->top->data;
    s->top = s->top->preNode;
    return true;
}

int main(int argc, const char *argv[])
{
    freopen("input.txt", "r", stdin);
    Stack stack;
    int T;
    char ps[MAX];

    cin >> T;
    for (int tc = 1; tc < T + 1; tc++)
    {
        initStack(&stack);

        cin >> ps;
        // int i= -1;
        cout << ps ;
        for(int i=0; i<strlen(ps); i++)
        {
            cout << ps[i] << " ";
            if (ps[i] == ')')
            {
                if (!(pop(&stack)))
                {
                    pushBack(&stack, ps[i]);
                    break;
                }
            }
            else
            {
                pushBack(&stack, ps[i]);
            }
        }
        isEmpty(&stack) ? cout << "YES" : cout << "NO";
        cout << endl;
    }
}