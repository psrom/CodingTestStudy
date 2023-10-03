# https://www.acmicpc.net/problem/21608
N = int(input())
classroom = [[0] * N for _ in range(N)]
students = [list(map(int, input().split())) for _ in range(N ** 2)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for student in students:
    like_list = student[1:]
    available = []

    for i in range(N):
        for j in range(N):
            if classroom[i][j] == 0:
                like, empty = 0, 0

                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if 0 <= nx < N and 0 <= ny < N:
                        if classroom[nx][ny] in like_list:
                            like += 1

                        if classroom[nx][ny] == 0:
                            empty += 1

                available.append((i, j, like, empty))

    available.sort(key=lambda x: (-x[2], -x[3], x[0], x[1]))
    classroom[available[0][0]][available[0][1]] = student[0]

answer = 0
scores = [0, 1, 10, 100, 1000]
students.sort()

for i in range(N):
    for j in range(N):
        cnt = 0

        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if 0 <= nx < N and 0 <= ny < N:
                if classroom[nx][ny] in students[classroom[i][j] - 1]:
                    cnt += 1

        answer += scores[cnt]

print(answer)
