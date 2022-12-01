#조건식의 결과물들을 하나로 합쳐주는 연산자

# and : 논리곱. 서로 다른 조건을 만족하는 유일한 하나를 찾음
print(True+1, False+1) #논리값 True : 1, False : 0 
print(True and True) # =print(1 and 1)
print(True and False) # =print(1 and 0)
#  -> 논리곱은 산술연산의 곱셈과 비슷한 처리 방식으로 연산됨

# or : 논리합. 서로 비슷한 조건들 중 하나를 만족하는 여러개를 찾음
print(1 or 0)
print(0 or 1)
print(1 or 1)
print(1.0 or 1)
#  -> 논리 합은 덧셈과 '비슷한' 논리임
#  -> 무조건 True/False 결과만 나오니 주의. 같지 않음!

# not : 부정. 긍부부, 부부긍 (긍정의 부정은 부정, 부정의 부정은 긍정)
print(not True, not False)

# 관계연산자가 2개 이상 필요하다면? 증명하면 됨.
x=5
print(3 < x < 10)
print(x > 3 and x < 10) # 논리연산은 관계연산보다 낮음.(연산이 꼬일 걱정은 하지 않아도 됨)


