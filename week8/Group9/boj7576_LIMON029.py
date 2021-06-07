from collections import deque

def bfs(box, M, N):
    q = deque()
    days = -1

    # 상하좌우 탐색 시 쓰일 리스트
    direction_x = [0, -1, 0, 1]
    direction_y = [1, 0, -1, 0]

    # 이미 익어있는 토마토의 위치 저장
    for i in range(N):
        for j in range(M):
            if box[i][j] == 1:
                q.append([j, i])

    while q:
        xy = q.popleft()  # 익은 토마토 위치 찾기
        for i in range(4):  # 상하좌우 탐색
            curr_x = xy[0] + direction_x[i]
            curr_y = xy[1] + direction_y[i]
            if 0 <= curr_x < M and 0 <= curr_y < N:
                if box[curr_y][curr_x] == 0:
                    q.append([curr_x, curr_y])
                    box[curr_y][curr_x] = box[xy[1]][xy[0]] + 1

    for items in box:
        for item in items:
            if item == 0:
                return -1
            days = max(days, item)

    return days - 1


M, N = map(int, input().split())
box = [list(map(int,input().split())) for y in range(N)]

print(bfs(box, M, N))