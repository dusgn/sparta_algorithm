"""
순차 탐색을 하며 저장을 어떻게 해야 할까?
내가 푼 것
def is_correct_parenthesis(string):
    open_str = 0
    close_str = 0
    for s in string:
        if s == "(":
            open_str += 1
        else:
            open_str -= 1

    if open_str == 0:
        return True
    else:
        return False

이렇게 생각해 보자 바로 직전에 조회한 괄호를 저장해야 한다. -> 스택

string="(()"
삽입된 문자열을 차례로 스택에 쌓는다.
stack = ["(","("]
그러다 닫는 괄호를 발견 하게 되면 열린 괄호 한 개를 제거 한다.
 stack = ["("]
문자열을 다 돈 뒤 스텍이 비어있어야 짝이 모두 맞는 것
"""
s = "(())"


def is_correct_parenthesis(string):
    stack = []
    for i in range(len(string)):
        if string[i] == "(":
            stack.append(i) # 어떤 값이 들어가도 상관 X (여부만 알면 됨)
        elif string[i] == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()

    if len(stack) == 0 :
        return True
    else:
        return False


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!