from collections import deque

c = 11
b = 2


def catch_me(cony_loc, brown_loc):
    time = 0
    queue = deque()
    queue.append((brown_loc, 0))  # 위치와 시간 동시에
    visited = [{} for _ in range(200001)]  # 시간별 위치를 저장해줌

    while cony_loc <= 200000:
        cony_loc += time  # 시간 만큼 이동 함
        if time in visited[cony_loc]:
            return time

        for i in range(0, len(queue)):
            current_position, current_time = queue.popleft()

        new_time = current_time + 1
        new_position = current_position - 1
        if - 0 < new_position <= 200000:
            queue.append((new_position, new_time))

        new_position = current_position + 1
        if - 0 < new_position <= 200000:
            queue.append((new_position, new_time))

        new_position = current_position * 2
        if - 0 < new_position <= 200000:
            queue.append((new_position, new_time))

        time += 1
        return -1


print(catch_me(c, b))  # 5가 나와야 합니다!
