#문자열의 연산기능을 이용하면, 화면에 보여주는 것을 좀 더 간편하게 할 수 있음

name1="홍길동"
age1=39
hobby1="코딩"
size=22
#곱연산 : 매번 수동으로 고치지 않겠다는 것
print("-"*size)
print("이름\t|나이\t|취미")
print("-"*size)
print(name1,"\t|",age1,"\t|",hobby1) #이렇게 하면 결과에서 한 칸씩이 밀리게 됨
print("-"*size)

#합연산 : 값을 좀 더 유연하게 이용하겠다
print(name1+"\t|"+str(age1)+"\t|"+hobby1) #합연산을 사용해서 해결!
#단, 문자값과 숫자값은 서로 더할 수 없으므로 str을 사용함

#print 팁 : 짧으면 합쳐서 사용하자
#기준은 마음대로지만, 화면 절반을 넘어서는가로 잡아서 판단하는 편임
#싫으면 합치지 않아도 됨


#실습문제2

#답2-1

print("\"QUICK\" Brown \"Fox\"")
print("="*19)
print("JUMP \'over\'")
print("="*11)
print("\"the \\LAZY\\ DOG\".")
print("="*17)

#답2-2
print("\"QUICK\" Brown \"Fox\"\n"+"="*19)
print("JUMP \'over\'\n"+"="*11)
print("\"the \\LAZY\\ DOG\".\n"+"="*17)

#문자열 밑에 밑줄처럼 연동시켜서 처리하고 싶다
#-> len()함수를 이용함

msg="\"the \\LAZY\\ DOG\"."
count=len(msg) #문자열 같은 것들의 길이(크기)를 구해준다.
print(msg)
print("="*count)

msg=input("입력받은 값만큼 나오게 해주세요:")
count=len(msg) 
print(msg)
print("="*count)

#실습문제3
#답3-1
print("파이썬은 \"쉽습니다.\"\n"
      "Python is \'SIMPLE\'\n\n"
      "\"다양한 방법을 시도하세요.\"")
#답3-2
#팁1 : 큰 다옴표 내부에서는 작은따옴표, 큰 따옴표 단독 사용은 어지간한 경우 문자로 취급된다
#->정 힘들면, 따옴표를 3번 찍자.
print("""파이썬은 "쉽습니다"\nPython is 'SIMPLE'\n\n"다양한 방법을 시도하세요.\"""")
#result="""파이썬은 "쉽습니다"\nPython is 'SIMPLE'\n\n"다양한 방법을 시도하세요.\""""
#print(repr(result))

#팁2 : 큰 따옴표 내부에서는 작은 따옴표는 무조건 문자로 취급되고,
#      작은 따옴표 내부에서는 큰 따옴표는 무조건 문자로 취급된다
print("'이것'",'"이것"')

#따옴표를 고치는 것보다 이스케이프를 쓰는 것이 빠르면, 그때는 이스케이프 문자를 쓰면 됨



#실습문제4

#본질은 숫자 연산과 같은 말임
#숫자에서는, 하나의 수치로 바꾸는 것
#문자에서는, 그 형태를 그대로 남겨두는 것

#답4-1
print("-- 값의 입력구간 : --")
count=int(input("큐브 크기 입력 :"))
box=str("ㅁ")
print("-- 값의 출력구간 --")
print((str(box)*count+"\n")*count)

#답4-2
size=int(input("큐브의 크기 입력 >>"))
print(("ㅁ"*size+"\n")*size)

         



