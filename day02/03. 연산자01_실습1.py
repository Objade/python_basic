# 산술 연산자
num1=10

# 일부를 제외한 대부분의 연산자의 사용규칙
#1. 한번 쓰면 필요한 곳에 바로 사용한다.
print("result1 :", num1+3)
      
#2. 여러번 사용되면 변수에 저장하여 사용한다.
# -> 해당 시점에서 연산된 '결과물'을 계속 이용한다
result2=num1-3 #num1-3(=7) -> 코드임.
print("result2 :",result2)
num1=8
print("result3 :", result2,num1-3)
#result2의 값은 7로 저장되어 있음.
# -> 이후에 변수(num1)이 바뀌더라도 result2의 값을 직접 바꾸지 않는 이상 result2의 값은 변하지 않음
print(result2)


#산술연산자의 주의사항
#1. 실수가 있으면 무조건 실수결과이다.
print("resutlt4 :",2.5*num1)

#2. 나누기는 무조건 실수값이다.
print(num1,"/ 2 =",num1/2)
print(num1,"/2.5 =",num1/1.6)

#3. 몫/나머지는 정수끼리는 정수값이다.
num2=3
print(num1, "//", num2, "=",num1 // num2)
print(num1, "%", num2, "=",num1 % num2)
num2=3.0
print(num1, "//", num2, "=",num1 // num2)
print(num1, "%", num2, "=",num1 % num2)
print(num1**1.5) #거듭제곱은 실수값 무관
print(3.14**0.5)


#4.(공통규칙) 연산자에는 우선순위가 존재함.
# 같은 카테고리 내 연산자끼리 우선순위
# 카테고리 단위로 우선순위가 존재함.
# ** > * > / > // >  % > + > -
# *와 나누기, +와-의 순서는 배치에 따라서 달라지기도 함
# -> 카테고리 단위로 기억하고, 헷갈리기 때문에...
#    소괄호(우선순위 연산자)를 붙여서 사용하자.

print("result5 :", 90+91+90/3)
print("result5 :", (90+91+90)/3)

print("실습문제")
      
print("100 + 3 =",100+3)
print("100 - 3 =",100-3)
print("100 * 3 =",100*3)
print("100 / 3 =",100/3)
print("100 // 3 =",100//3)
print("100 % 3 =",100%3)
print("100 ** 3 =",100**3)


#변수를 준비했다 : 철저하게 사용한다.
#->변수에 저장된 값이 바뀌면 그에 연동되도록 만든다.

#주의사항 : 중복된다고 무조건 변수는 아님.
num1=100
num2=3
print("100 + 3 =",num1 + num2)
print("100 - 3 =",num1 - num2)
print("100 * 3 =",num1 * num2)
print("100 / 3 =",num1 / num2)
print("100 // 3 =",num1 // num2)
print("100 % 3 =",num1 % num2)
print("100 ** 3 =",num1 ** num2)

print(num1, "+",num2,"=",num1 + num2)
print(num1, "-",num2,"=",num1 - num2)
print(num1, "*",num2,"=",num1 * num2)
print(num1, "/",num2,"=",num1 / num2)
print(num1, "//",num2,"=",num1 // num2)
print(num1, "%",num2,"=",num1 % num2)
print(num1, "**",num2,"=",num1 ** num2)

