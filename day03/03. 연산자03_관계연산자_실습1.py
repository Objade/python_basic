#관계연산자가 사용된 것을 조건식이라고 부름
#연산결과값으로 True/False라는 Bool(Boolean)값이 나옴

#크기 비교는 오로지, 수치에 대해서만 가능함
#문자값과는 일치/불일치만 체크할 수 있음

num1=10
num2=5
print(num1, ">", num2, ":", num1 > num2)
print(num1, "<", num2, ":", num1 < num2)
print(num1, ">=", num2, ":", num1 >=num2)
print(num1, "<=", num2, ":", num1 <= num2)
print(num1, "==", num2, ":", num1 == num2)
print(num1, "!=", num2, ":", num1 != num2)

#관계연산자를 2개 이상 쓰지 말 것.
#파이썬만 2개 이상 쓸 수 있음 (다른 언어에서는 불가능)

x=5
print(3 < x < 10) # 파이썬 ~> 3<x, x<10 알아서 분리시켜줌
#파이썬 외의 언어들은 무조건 2개씩만 처리함. 동시 처리가 안됨

print(3<x, x<10) #어지간한 경우에는 조금 곤란함

#그러면 어떻게 합치나? 논리 연산자.



