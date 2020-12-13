input = "abcabcabcabcdededededede"
"""
압축할 문자열 중 가장 짧은 것의 길이를 반환해야 함
1로 짜를지 2로 짜를지 3으로 짜를지 패턴을 분석해야함 
 > 모든 경우를 파악해 최솟값 반환
"""

"""
splited = [
            string[i:i + split_size] for i in range(0, n, split_size)
        ]
        
위 아래 같음       
        
splited = []
for i in range(0, n, split_size):
    splited.append(string[i:i+split_size])
"""


def string_compression(string):
    n = len(string)
    compression_length_array = []

    for split_size in range(1, n // 2):
        compressed = ""
        splited = [
            string[i:i + split_size] for i in range(0, n, split_size)
        ]
        count = 1
        # 이전 값과 자신을 비교하기 때문에 이미 나는 나와잇어서 1

        # 이전값과 현재값 비교를 위해 1부터
        for j in range(1, len(splited)):
            prev, cur = splited[j - 1], splited[j]
            if prev == cur:
                count += 1
            else:
                if count > 1:  # 압축을 해야한다
                    compressed += (str(count) + prev)  # ex) 2abc
                else:
                    compressed += prev
                count = 1
        # 남은 꼬다리 처리
        if count > 1:
            compressed += (str(count) + splited[-1])
        else:
            compressed += splited[-1]
            # print(compressed)
        compression_length_array.append(len(compressed))

    return min(compression_length_array)


print(string_compression(input))
