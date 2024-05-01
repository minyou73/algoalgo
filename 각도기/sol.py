# 각 angle이 매개변수로 주어질 때 예각일 때 1, 직각일 때 2, 둔각일 때 3, 평각일 때 4를 return하도록 solution 함수를 완성해주세요.

def solution(angle):
    if 0 < angle < 90:
        return 1 #예각
    elif angle == 90 :
        return 2 #직각
    elif 90 < angle < 180 :
        return 3 #둔각
    elif angle == 180 :
        return 4 #평각

print(solution(70))
print(solution(91))