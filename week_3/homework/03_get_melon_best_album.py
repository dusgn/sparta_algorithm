"""
1. 속한 노래가 많이 재생된 장르를 먼저 수록한다.
        장르별 재생 횟수를 더해야 한다.
        장르(key)별로 재생된 횟수(value)를 저장
2. 장르 내에서 많이 재생된 노래를 먼저 수록한다.
        장르내에서 정렬 필요
        장르별 Key 에, 재생 수와 인덱스를 배열로 묶어 배열에 저장

3. 장르 내에서 재생회수가 같다면 고유 번호가 낮은 노래 먼저 수록한다.


"""
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

def get_melon_best_album(genre_array, play_array):
    n = len(genre_array)
    genre_total_play_dict = {}
    genre_index_play_array_dict = {}
    for i in range(n):
        genre = genre_array[i]
        play = play_array[i]
        if genre not in genre_total_play_dict:
            genre_total_play_dict[genre] = play
            genre_index_play_array_dict[genre] = [[i, play]]
        else:
            genre_total_play_dict[genre] += play
            genre_index_play_array_dict[genre].append([i, play])

    sorted_genre_play_array = sorted(genre_total_play_dict.items(), key=lambda item: item[1], reverse=True)
    result = []
    for genre, _value in sorted_genre_play_array:
        index_play_array = genre_index_play_array_dict[genre]
        sorted_by_play_and_index_play_index_array = sorted(index_play_array, key=lambda item: item[1], reverse=True)
        for i in range(len(sorted_by_play_and_index_play_index_array)):
            if i > 1:
                break
            result.append(sorted_by_play_and_index_play_index_array[i][0])
    return result


print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!