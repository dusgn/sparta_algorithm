k = 4  # 말의 개수

#각 칸마다 스택을 놓고 움직이는건 어떨까

chess_map = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
start_horse_location_and_directions = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
# 이 경우는 게임이 끝나지 않아 -1 을 반환해야 합니다!
# 동 서 북 남
# →, ←, ↑, ↓
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]


# 말은 순서대로 이동합니다 - > 말의 순서에 따라 반복문
# 말이 쌓일 수 있습니다 -> 맵에 말이 쌓이는걸 저장해야함
# 쌓인 순서대로 이동한다 -> stack을 쓰자
# 현재 맵에 어덯게 말이 쌓일지를 저장하기 위해
# chess_map

def get_d_idx_when_go_back(d):
    if d % 2 == 0:
        return d + 1
    else:
        return d - 1


def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions):
    n = len(chess_map)
    turn_count = 1
    current_stacked_horse_map = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(horse_count):
        r, c, d = horse_location_and_directions[i]
        current_stacked_horse_map[r][c].append(i)

    while turn_count <= 1000:
        for horse_idx in range(horse_count):
            r, c, d = horse_location_and_directions[horse_idx]
            new_r = r + dr[d]
            new_c = c + dc[d]

            # 3) 파란색인 경우에는 A번 말의 이동 방향을 반대로 하고 한 칸 이동한다.
            if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:
                new_d = get_d_idx_when_go_back(d)

                horse_location_and_directions[horse_idx][2] = new_d
                new_r = r + dr[new_d]
                new_c = c + dc[new_d]
                # 3) 방향을 반대로 바꾼 후에 이동하려는 칸이 파란색인 경우에는 이동하지 않고 가만히 있는다.
                if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:
                    continue

            # 2가 이동한다고 치면, 2랑 3만 이동
            # 즉, 자기자신의 인덱스보다 큰 애들만 데리고 감
            # [1, 2, 3] [:i]
            moving_horse_idx_array = []
            for i in range(len(current_stacked_horse_map[r][c])):
                current_stacked_horse_idx = current_stacked_horse_map[r][c][i]
                if horse_idx == current_stacked_horse_idx:
                    moving_horse_idx_array = current_stacked_horse_map[r][c][i:]
                    current_stacked_horse_map[r][c] = current_stacked_horse_map[r][c][:i]
                    break

            if game_map[new_r][new_c] == 1:
                moving_horse_idx_array = reversed(moving_horse_idx_array)

            for moving_horse_idx in moving_horse_idx_array:
                current_stacked_horse_map[new_c][new_r].append(moving_horse_idx)
                horse_location_and_directions[moving_horse_idx][0], horse_location_and_directions[moving_horse_idx][1] = new_r, new_c

            if len(current_stacked_horse_map[new_r][new_c]) >= 4:
                return turn_count

        turn_count += 1
    return -1


print(get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))  # 2가 반환 되어야합니다
