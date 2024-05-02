# 머쓱이네 옷가게는 10만 원 이상 사면 5%, 30만 원 이상 사면 10%, 50만 원 이상 사면 20%를 할인해줍니다.
#구매한 옷의 가격 price가 주어질 때, 지불해야 할 금액을 return 하도록 solution 함수를 완성해보세요.

def solution(price):
    if  300000 > price >= 100000:
        return int(price * 0.95)

    elif 500000 > price >= 300000:
        return int(price * 0.9)

    elif price >= 500000:
        return int(price * 0.8)

    else:
        return price

print(solution(150000))
print(solution(100010))

############################################################

def solution(price):
    discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
    for discount_price, discount_rate in discount_rates.items():
        if price >= discount_price:
            return int(price * discount_rate)