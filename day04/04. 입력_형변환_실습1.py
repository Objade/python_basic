#형변환은 값의 자료형을 바꾸는 것
#-> 값이기만 하면 다 할 수 있음

#운용요령 : 연산자랑 동일한 방식으로 사용함
#          단, 같은 자료형으로는 바꾸지 않음

#1. int(값) : 괄호 안의 값을 '정수값' 으로 바꿔서 준비해줌
# -> '정수 형태' 의 문자열만 바꿀 수 있음
# -> 실수값을 소수점 버림처리 하며 정수로 바꿀 수 있음 (반올림X, 버림처리)
value="123" 
print(int(value)+5) #한번 쓸 때

value=int(value) #원본이 필요 없을 때
_value=int(value) #원본이 필요할 때

print(int(value)+int(value)) #여러 번 쓸 때

value=3.14
print(int(value)+5)
print(int(value + value))

#2. float(값) : 실수값으로 바꿈
#  -> int가 형변환 할 수 있는 것을 다 실수값으로 바꿈
#  -> 실수형태의 문자열을 바꿀 수 있음
#  -> 정수값을 바꾸면 소수점이 붙는데, 굳이 안함.
#     ☆들어오는 값에 대해서, 실수값을 보장하고 싶을 때 사용.
#  -> int 형태보다 좀 더 융통성이 좋음

value="3.14"

print(float(value) + 5)
value=float(value)
print(value + value)

#cf) "3.14" > 문자값 / 3.14 > 숫자값(수치연산 가능)

#3. str(값) : 문자열 값으로 바꿈
#  -> 다 됨, 못바꾸는 것이 거의 없음.
#  -> 문자열 값으로 다루기 위해 필요한 것이 아니면, 굳이 사용하지 않음
#  -> 문자열은 저장외에도 융통성이 좋아서 값의 모양을 편하게 바꾸고 싶을 때 자주 사용됨

result=str(print)
print(result + "A")

print(3.14**(0.5))

result=3.14**(0.5)
print(result)
result=str(result) [:5]
print(result)
result=float(result)
print(result+5)

#input과 연계하여 사용하려면?

#ex1)

num=input("정수값 입력 >>")
print("5를 더한 결과 :", int(num)+5)

#ex2)

fnum=input("실수값 입력 >>")
fnum=float(fnum)
print("정수부 :", fnum//1)
print("실수부 :", fnum%1)

#ex2-1)

fnum=float(input("실수값 입력 >>"))
print("정수부 :", fnum//1)
print("실수부 :", fnum%1)



