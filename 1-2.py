import queue

#상태를 나타내는 클래스
class State:
    def __init__(self, board, goal, moves=0):
        self.board = board
        self.moves = moves
        self.goal = goal
        
    # i1과 i2를 교환하여 새로운 상태를 반환
    def get_new_board(self, i1, i2, moves):
        new_board = self.board[:]
        new_board[i1], new_board[i2] = new_board[i2], new_board[i1]
        return State(new_board, self.goal, moves)
        
    #자식 노드를 확장하여서 리스트에 저장하여 반환
    def expand(self, moves):
        result = []
        i = self.board.index(0)
        if not i in [0, 1, 2] :
            result.append(self.get_new_board(i, i-3, moves))
        if not i in [0, 3, 6] :
            result.append(self.get_new_board(i, i-1, moves))
        if not i in [2, 5, 8] :
            result.append(self.get_new_board(i, i+1, moves))
        if not i in [6, 7, 8] :
            result.append(self.get_new_board(i, i+3, moves))
        return result
    
    # f(n)을 계산하여 반환
    def f(self):
        return self.h()+self.g()
    
    # 휴리스틱 함수 값인 h(n)을 계산하여 반환
    # 현재 제 위치에 있지 않은 타일의 개수를 리스트의 함축으로 계산한다.
    def h(self):
        return sum([1 if self.board[i] != self.goal[i] else 0 for i in range(8)])
    
    # 시작 노드로부터의 경로를 반환
    def g(self):
        return self.moves
    
    # 상태와 상태를 비교하기 위하여 less than 연산자를 정의
    def __lt__(self, other):
        return self.f() < other.f()
    
    # 객체를 출력할 때 사용
    def __str__(self):
       return "-------------------- f(n)=" + str(self.f()) +"\n"+\
       "-------------------- h(n)=" + str(self.h()) +"\n"+\
       "-------------------- g(n)=" + str(self.g()) +"\n"+\
       str(self.board[:3]) + "\n" +\
       str(self.board[3:6]) + "\n" +\
       str(self.board[6:])+ "\n" +\
       "----------------------"
                
# 초기 상태
puzzle = [1, 2, 3,
          0, 4, 6,
          7, 5, 8]
                
# 목표상태
goal = [1, 2, 3,
        4, 5, 6,
        7, 8, 0]
                
# open 리스트는 우선순위 큐로 생성
open_queue = queue.PriorityQueue()
open_queue.put(State(puzzle, goal))
                
closed_queue = []
moves = 0
while not open_queue.empty():
    
    current = open_queue.get()
    print(current)
    if current.board == goal:
        print("탐색 성공")
        break
    moves = current.moves+1
    for state in current.expand(moves):
        if state not in closed_queue:
            open_queue.put(state)
    closed_queue.append(current)
else:
    print('탐색 실패')