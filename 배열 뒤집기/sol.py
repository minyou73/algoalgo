# 정수가 들어 있는 배열 num_list가 매개변수로 주어집니다. num_list의 원소의 순서를 거꾸로 뒤집은 배열을 return하도록 solution 함수를 완성해주세요.

def solution(num_list):
    
    return num_list[::-1]


print(solution([1, 2, 3, 4, 5]))


####################################################

def solution(num_list):
    result = []
    while(num_list):
        result.append(num_list.pop())
    return result

####################################################

def solution(num_list):
    num_list.reverse()