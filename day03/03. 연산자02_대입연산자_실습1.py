#대입연산자 : 단독사용을 해야 하는 연산자
#연산자로써의 특징 : 오른쪽부터 처리됨
num=5

#result=10+(num=20)  -> 이런건 못함

result=num=10 #-> 이런건 가능
print(result, num)

#print(result, num=20) -> 이런건 못함

#수치연산자가 아니다 보니 '단독 사용'을 해야만 함


#오른쪽부터 처리가 되기 때문에 이런 것을 할 수 있음
result=result+11  #'result=11'의 연산을 먼저 처리함
#변수는 기본 사용시, 값만 불러옴
#단, 대입 연산자 왼쪽에 오면 오로지 저장공간/ 오른쪽에 오면 오로지 값.
print(result)
result=result-5
print(result)

#복합대입연산자 : 위의 형태의 연산을 줄여쓴 것
result-=5 #result=result-(5)
print(result)

#대입 : 변수의 '생성' 및 저장된 값의 '교체'
#복합 : 저장된 값의 '갱신' 및 '누적'
