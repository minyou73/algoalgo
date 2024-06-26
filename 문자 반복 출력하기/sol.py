# 문자열 my_string과 정수 n이 매개변수로 주어질 때, 
# my_string에 들어있는 각 문자를 n만큼 반복한 문자열을 return 하도록 solution 함수를 완성해보세요.

def solution(my_string, n):
    result = ''
    for char in my_string:
        for _ in range(n):
            result += char
    return result

# 예시 실행
print(solution("hello", 3))


##############################################

def solution(my_string, n):
    return ''.join(i*n for i in my_string)


##############################################

def solution(my_string, n):
    answer = ''
    for s in my_string:
        answer += s * n
    return answer