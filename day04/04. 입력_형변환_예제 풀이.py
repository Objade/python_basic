#값의 종류를 판단할 때 기준
# -> 실생활에서 어떤 식으로 표현되고 어떤 식으로 사용되고 있나?
# -> 프로그램은 현실의 문제를 해결하기 위해서 등장한 것

#입력시 안내 문자열은 매우 중요함.

#실습문제 1

#답1-1
byear=input("태어난 연도 입력 :") 
print("세는 나이:", 2022-int(byear)+1)
print("만나이(생일 후) :", 2022-int(byear))
print("만나이(생일 전) :", 2022-int(byear)-1)

#답1-2
byear=int(input("태어난 연도 입력 :")) 
print("세는 나이:", 2022-byear+1)
print("만나이(생일 후) :", 2022-byear)
print("만나이(생일 전) :", 2022-byear-1)

#답1-3
byear=int(input("태어난 연도 입력 :")) 
age=2022-int(byear)
print("세는 나이:", age+1)
print("만나이(생일 후) :", age)
print("만나이(생일 전) :", age-1)


#실습문제 2

#답2-1
print("600KG 기준 적재가능 화물갯수") 
weight=input("화물의 무게 입력(KG):")
print("적재가능수량 :",600/float(weight),"개")

#답2-2
print("600KG 기준 적재가능 화물갯수") 
weight=input("화물의 무게 입력(KG):")
count=600/float(weight)
print("적재가능수량 :",count,"개")

#답2-3
print("600KG 기준 적재가능 화물갯수") 
weight=float(input("화물의 무게 입력(KG):"))
count=600/weight
print("적재가능수량 :",count,"개")

#답2-4
print("600KG 기준 적재가능 화물갯수") 
weight=float(input("화물의 무게 입력(KG):"))
count=600/weight
print("적재가능수량 :",int(count),"개")


#실습문제 3

#답3-1
height=input("키 입력(m)")
print("남성 표준:", float(height)*float(height)*22,"KG")
print("여성 표준:", float(height)*float(height)*21,"KG")

#답3-2
height=input("키 입력(m)")
mweight=float(height)*float(height)*22
wweight= float(height)*float(height)*21
print("남성 표준:",mweight,"KG")
print("여성 표준:",wweight,"KG")

#답3-3
height=float(input("키 입력(m)"))
mweight=height*height*22
wweight=height*height*21
print("남성 표준:",mweight,"KG")
print("여성 표준:",wweight,"KG")

#답3-4
height=float(input("키 입력(m)"))
mweight=height**2*22
wweight=height**2*21
print("남성 표준:",mweight,"KG")
print("여성 표준:",wweight,"KG")

#답3-5
value=float(input("키 입력(m)"))**2
print("남성 표준:",value*22,"KG")
print("여성 표준:",value*21,"KG")


#->정확한 결과값을 구하는 것은 좋지만, 필요한 만큼만/형태로 바꿔줘야 함

