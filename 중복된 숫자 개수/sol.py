# 정수가 담긴 배열 array와 정수 n이 매개변수로 주어질 때, array에 n이 몇 개 있는 지를 return 하도록 solution 함수를 완성해보세요.

def solution(array, n):
    count = 0
    for i in array:
        if i == n:
            count += 1

    return count

print(solution([1, 1, 2, 3, 4, 5], 1))

################################################################

def solution(array, n):
    result = []
    for element in array:
        if element == n:
            result.append(n)
    
    return len(result)

###########################################################

def solution(array, n):
    return array.count(n)
