#팁 : 일단 작성하고, 중첩되는 것은 변수로 뺀다.

#1. 90, 90, 91의 합과 평균을 구해서 출력하세요
#ex) 합: XXX, 평균 : XX.YYYYYYYYYYYYYYY

num1=90
num2=91
result1=num1*2+num2
result2=result1/3
print("합 :", result1)
print("평균 : ",result2)

#2. 1번에서 구한 평균에서 정수부와 실수부를 분리하여 출력하세요.
#ex) 정수부 : XX.0 (또는 XX)
#    실수부 : 0. YYYYYYYYY
result3=result1//3
print("정수부 :", result3)
print("실수부 :", result2-result3)

#3. 2번에서 구한 정수부와 실수부의 곱을 출력하세요
#ex) 두 값의 곱 : AA.BBBBBBBBBBBB
result4=result2-result3
result5=result3*result4

print("두 값의 곱 :", result5)


#4. 3번에서 구한 곱의 결과와 1번에서 구했던 세 정수와의 합을 더한 결과를 출력하세요
#ex) 마지막 결과 : CCC.BBBBBB
print("마지막 결과 :", result1+result5)


#결과
num1=90
num2=91
result1=num1*2+num2
result2=result1/3
result3=result1//3
result4=result2-result3
result5=result3*result4 #굳이 필요하지는 않음

print("합 :", result1)
print("평균 : ",result2)
print("정수부 :", result3)
print("실수부 :", result2-result3)
print("두 값의 곱 :", result5)
print("마지막 결과 :", result1+result5)



#정리
#변수 사용 요령
#1. 두번 이상 사용되면 변수다.
#2 철저하게 사용해라.  연동이 되도록.

#복습 요령
#1. 직접 코드를 작성해봐야 된다.
#2. 거듭해서 복습해라.
#3. 노트에 손으로 필기하는 것도 도움이 됨.


