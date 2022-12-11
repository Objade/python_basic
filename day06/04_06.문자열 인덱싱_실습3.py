#추가 문제

#실수값은 연산을 통해서 나오지만, 소수점이 너무 많음
#어떤 값이 들어오더라도, 소수점 2자리까지만 출력되도록
#메서드와 슬라이싱을 응용해서 처리해보자.

#팁
value="3.1"
print(value[1:8]) #범위를 넓게 잡아도, 더 짧으면 알아서 멈춤.

fnum1=float(input("실수1 입력 >>"))
fnum2=float(input("실수2 입력 >>"))

#답1
fnum3=str(fnum1/fnum2)
answer=fnum3.replace(fnum3[4:],"")
print("fnum1/fnum2 :", answer)

#답2 
value=str(fnum1/fnum2)
i=value.index(".")
print("fnum1/fnum2 :", value[:i+3])

#슬라이싱은 범위를 초과해도 알아서 멈춤

#추가 문제 2

#임의의 실수값 2개를 입력 받는다.
#입력을 받은 두 실수값을 곱하여 연산한다.
#연산한 결과에 대해서 정수부는 분리하여 정수값으로 준비한다.
#실수부는 최대 3자리 까지만 가져오고, 1000을 곱한 다음 정수값으로 이용한다.
# 구한 두 정수의 합을 출력하시오.

#ex)113.244546527
#정수부 : 113
#실수부를 바꾼 값 : 244
#두 수의 합 : 357

#답1 #수치 연산은 숫자로 하는 것이 제일 편하고 좋음
fn1=float(input("실수1 입력 :"))
fn2=float(input("실수2 입력 :"))

value=fn1*fn2
num1=int(value)
num2=int(value%1*100)

print("나눈 값 :", value)
print("두 정수 :", num1,num2)
print("두 수의 합 :", num1+num2)

#답2 #문자열로 바꾸는 이유는, 모양을 건드리는 것이 주 목적이다.

value=str(value)
i=value.index(".")
num1=int(value[:i])
num2=value[i+1:i+4]
count=3-len(num2)
num2+="0"*count
num2=int(num2)

print("나눈 값 :", value)
print("두 정수 :", num1,num2)
print("두 수의 합 :", num1+num2)

#답3
value=str(value)
i=value.index(".")
num1=int(value[:i])
num2=int(value[i+1:i+4]+"0"*(3-len(value[i+1:i+4])))

print("두 수의 곱 :", value)
print("정수부 :", num1)
print("실수부 :", num2)
print("두 수의 합 :", num1+num2)






