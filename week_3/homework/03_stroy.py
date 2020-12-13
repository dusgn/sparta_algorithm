"""
규칙을 다시 한 번 곱씹고 가겠습니다.

1. 속한 노래가 많이 재생된 장르를 먼저 수록한다.
2. 장르 내에서 많이 재생된 노래를 먼저 수록한다.
3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록한다.

가장 많이 → 정렬을 해야 한다! 라는 의미로 보시면 됩니다.

우선, 속한 노래가 가장 많이 재생된 장르를 찾아보겠습니다.
그걸 알기 위해서는 장르별 재생 수를 더해야 하는데,
장르별(Key) 로 재생 수(Value)를 더하고 관리하기 위해서는
딕셔너리를 쓰시면 됩니다!
"""
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def get_melon_best_album(genre_array, play_array):
    n = len(genre_array)
    genre_total_play_dict = {}
    for i in range(n):
        genre = genre_array[i]
        play = play_array[i]
        if genre not in genre_total_play_dict:
            genre_total_play_dict[genre] = play
        else:
            genre_total_play_dict[genre] += play

    print(genre_total_play_dict)
# {'classic': 1450, 'pop': 3100} 이 출력됩니다!

"""
자 그런데, 여기서 끝이 아닙니다.
저희는 장르 내에서 많이 재생된 노래를 수록해야 하므로,
장르 내에서의 정렬도 필요합니다!

장르 별 곡의 정보를 저장하기 위해서는 어떡할까요?
바로 장르별 Key 에, 재생 수와 인덱스를 배열로 묶어 배열에 저장해두면 됩니다!

왜 재생 수와 인덱스를 저장하냐면,
재생 수로 정렬을 해야 하고,
들어가는 노래의 인덱스를 반환해야 해서
둘 다 필요하기 때문입니다!
"""

```python
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

def get_melon_best_album(genre_array, play_array):
    n = len(genre_array)
    genre_total_play_dict = {}
    **genre_index_play_array_dict = {}**
    for i in range(n):
        genre = genre_array[i]
        play = play_array[i]
        if genre not in genre_total_play_dict:
            genre_total_play_dict[genre] = play
            **genre_index_play_array_dict[genre] = [[i, play]]**
        else:
            genre_total_play_dict[genre] += play
            **genre_index_play_array_dict[genre].append([i, play])**

    print(genre_total_play_dict)
    # {'classic': 1450, 'pop': 3100} 이 출력됩니다!
    print(genre_index_play_array_dict)
    # {'classic': [[0, 500], [2, 150], [3, 800]], 'pop': [[1, 600], [4, 2500]]} 이 출력됩니다!

"""
자, 이렇게 장르별 총 곡의 재생횟수와 장르별 곡의 인덱스와 재생 수를 저장했습니다!

그러면, 이제 재생 수가 많은 장르 별로 곡을 재생 수 별로 담으면 되는데,

가장 재생 수가 높은 장르를 어떻게 뽑을 수 있을까요?

그러기 위해선, 바로 genre_total_play_dict 을 정렬하시면 됩니다.

어떻게 딕셔너리를 정렬할 수 있을까요?

딕셔너리의 키 - 값을 배열 형태로 추출하는 방법이 있습니다.
바로 dict.items() 함수를 사용하시면 됩니다!

genre_total_play_dict.items() 를 보시면

`dict_items([('classic', 1450), ('pop', 3100)])` 이런 값을 주고 있습니다.

이 값을 정렬하기 위해서는, 어떤 기준으로 정렬을 해줄지 정해줘야 합니다!
'classic'이라는 **Key**, 1450 이라는 **Value** 가 있지만 
컴퓨터는 뭘로 정렬할지 알려주지 않으면 모릅니다!

정렬해주는 함수인 **sorted** 에는 그 기준을 정해주는 인자들이 있습니다.
**key** 라는 인자에 람다값을 전달하면 되는데,

어떤 것으로 정렬할지에 대해 정해주는 기준이라고 보시면 됩니다.
다음과 같이 **item[0]** 을 전달하시면, 'classic' 이라는 키로 정렬이 되고,
sorted(genre_total_play_dict.items(), key=lambda item: **item[0]**)

다음과 같이 **item[1]** 을 전달하시면, 1450 이라는 밸류 값을 기준으로 정렬이 됩니다.
sorted(genre_total_play_dict.items(), key=lambda item: **item[1]**)

또한 저희는 내림차순으로 밸류 값을 기준으로 정렬하고 싶기 때문에 아래처럼 reverse 인자를 설정해주시면 됩니다!
sorted(genre_total_play_dict.items(), key=lambda item: item[1], **reverse=True**)

* 어떤 것을 정렬할지에 대해 정해주는 sorted 함수의 key 부분에서 lambda 라는 파이썬 문법을 사용하는데, 현재 genre_total_play_dict 의 각 원소는 [인덱스 수, 플레이 수] 형태의 배열로 되어 있습니다. 그래서 이 중 어떤 걸 기준으로 정렬할 것이냐! 를 정해주는 코드라고 생각하시면 됩니다.
파이썬의 람다에 대해서는 한 번 구글링 해보면서 공부해보셔도 좋을 것 같습니다!
"""

		sorted_genre_play_array = sorted(genre_total_play_dict.items(), key=lambda item: item[1], reverse=True)
    print(sorted_genre_play_array)
# 그러면 이렇게 밸류값을 기준으로 정렬할 수 있습니다!
# [('pop', 3100), ('classic', 1450)]

"""
자, 이제 장르별 순위를 알 수 있게 되었고, 
장르별 곡 인덱스와 플레이 수도 저장해놨습니다! 

그럼 이걸 기반으로 각 장르별 1순위 2순위의 곡들을 
result 배열에 추가해서 반환해주시면 됩니다!

장르와 값들을 꺼내서, genre_index_play_array_dict 에서
index_play_array 값을 가져옵니다.
그러면 [[1, 600], [4, 2500]] 이런식으로 배열이 들어가 있는 걸 보실 수 있습니다!

[1, 600] 에서 1은 곡의 인덱스, 뒤의 값은 플레이 수 600입니다.
여기서 정렬을 해야 하는 기준은! 아까와 마찬가지로 두번째 값이죠? 그러면 
다음과 같이 정렬을 할 수 있습니다.

sorted(index_play_array, key=lambda item: item[1])

마찬가지로, 내림차순으로 정렬해줘야 합니다!

sorted(index_play_array, key=lambda item: item[1], reverse=True)

그리고 정렬된 배열 안에 있는 값들을 result 배열에 추가해줍니다.
이 때는 인덱스!! 를 반환해줘야 하기 때문에, 
sorted_by_play_and_index_play_index_array[i][0] 를 추가해주시면 됩니다.
"""

        for i in range(len(sorted_by_play_and_index_play_index_array)):
            if i > 1:
                break
            result.append(sorted_by_play_and_index_play_index_array[i][0])
    return result
"""
code
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


print(get_melon_best_album(genres, plays))