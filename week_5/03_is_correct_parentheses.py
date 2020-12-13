"""
 균형잡힌 괄호 문자열 > 올바른 괄호 문자열
 3주차 is_correct_parentheses

"""
from collections import deque

balanced_parentheses_string = "()))((()"


def is_correct_parentheses(string):  # 올바른 괄호인지 확인
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        elif stack:
            stack.pop()
    return len(stack) == 0  # 문자열이 끝나고 아무것도 안남으면 True


def reverse_parenthesis(string):
    # 4. 문자열 u가 올바른 괄호 문자열이 아니라면아래 과정을 수행
    # 4-1 빈 문자열에 첫번째 문자로 (를 붙임
    # 4-2 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어붙임
    # 4-3 )를 다시 붙임
    # 4-4 u의 첫번째 문자와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을
    # 뒤집어 뒤에 붙인다.
    reversed_string = ""
    for char in string:
        if char == '(':
            reversed_string += ')'
        else:
            reversed_string += '('
    return reversed_string


def separate_to_u_v(string):
    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u,v로 분리
    # 단 u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며
    # v는 빈 문자열이 될 수 있습니다.
    # 균형이 맞으려면 (, ) 갯수가 같아야 함
    queue = deque(string)
    left, right = 0, 0
    u, v = "", ""
    while queue:
        char = queue.popleft()
        u += char
        if char == '(':
            left += 1
        else:
            right += 1
        if left == right:
            break
    v = ''.join(list(queue))
    return u, v


def changed_to_correct_parenthesis(string):  # 균형 - > 올바른
    # 1. 입력이 빈 경우, 빈 문자열 반환
    if string == "":
        return ""
    # 2번 조건
    u, v = separate_to_u_v(string)

    # 3. 문자열 u가 올바른 괄호 문자열이라면 문자열 v에 대해
    # 1단계 부터 다시 시작 (change_to_correct_parenthesis를 다시함)
    # 3-1 수행한 결과 문자열을 u에 이어붙인 뒤 반환
    if is_correct_parentheses(u):
        return u + changed_to_correct_parenthesis(v)
    else:
        return "(" + changed_to_correct_parenthesis(v) + ")" + reverse_parenthesis(u[1:-1])


def get_correct_parentheses(balanced_parentheses_string):
    if is_correct_parentheses((balanced_parentheses_string)):
        return balanced_parentheses_string
    else:  # 균형잡혔지만 올바르진 않은 경우
        return changed_to_correct_parenthesis(balanced_parentheses_string)


print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!
