import sys
sys.stdin = open("../D4/input.txt", "r")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if not self.head:
            return True

        return False

    def push(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            return None

        ret_data = self.head.data

        self.head = self.head.next

        return ret_data

    def peek(self):
        if self.is_empty():
            return None

        return self.head.data

route = Stack()

def push_route(r, c):
    if r < 0 or c < 0:
        return False
    if r > 100 or c > 100:
        return False

    if maze[r][c] == 0 or maze[r][c] == 3:
        temp = {'x':r,'y':c}
        route.push(temp)
        return True
    return False


for tc in range(7,8):
    num = int(input())
    maze = []
    answer = True
    for i in range(100):
        lst = list(map(int,list(input())))
        if 2 in lst:
            startY = lst.index(2)
            startX = i
        maze.append(lst)
    location = {'x':startX,'y':startY}
    route.push(location)

    while(maze[location['x']][location['y']]!=3):
        flag = False
        row = location['x']
        col = location['y']
        print(f"point: {row}, {col}")
        print(f'stack: {route.peek()}')

        maze[row][col] = -1


        if(push_route(row+1,col)):
            location = route.peek()
            continue
        elif(push_route(row, col + 1)):
            location = route.peek()
            continue
        elif(push_route(row,col-1)):
            location = route.peek()
            continue
        elif (push_route(row - 1, col)):
            location = route.peek()
            continue
        print(f'막힘: {route.peek()}')


        if route.is_empty():
            answer = False
            break
        location = route.pop()


    if answer == False:
        print(f"#{tc} 0")
    else:
        print(f"#{tc} 1")

    route = Stack()