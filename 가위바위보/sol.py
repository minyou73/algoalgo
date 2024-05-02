# 가위는 2 바위는 0 보는 5로 표현합니다. 가위 바위 보를 내는 순서대로 나타낸 문자열 rsp가 
#매개변수로 주어질 때, rsp에 저장된 가위 바위 보를 모두 이기는 경우를 순서대로 나타낸 문자열을 return하도록 solution 함수를 완성해보세요.

def solution(rsp):
    r = 0
    s = 2
    p = 5
    result = ''

    for i in rsp:
        if i == "0":
            result += "5"
        elif i == "2":
            result += "0"
        elif i == "5":
            result += "2"

    return result

print(solution("205"))


####################################################

def solution(rsp):
    d = {'0':'5','2':'0','5':'2'}
    return ''.join(d[i] for i in rsp)


  