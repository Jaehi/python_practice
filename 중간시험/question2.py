def solution(price, grade):
    if grade == "S":
       return int(price-(price*0.05))
    elif grade == "G" :
       return int(price-(price*0.1))
    elif grade == "V" :
        return int(price-(price*0.15))
    
        
price = 2500
grade = "V"
d_price = solution(price, grade)# 금액은 소수점이 없기 때문에 int형으로 형변환을 해주었어요.

print(d_price)

print(grade,"회원님. ",price,"원 상품을 ",d_price,"원에 구매하세요!")

price = 96900
grade = "S"
d_price = int(solution(price, grade))

print(grade,"회원님. ", price, "원 상품을 ", d_price,"원에 구매하세요~")