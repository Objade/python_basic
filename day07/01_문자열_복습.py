# 실습1 
# 내가 입력한 단어의 첫문자와 끝문자를 합쳐서 출력하세요.

#답1-1
word=input("단어 :")
print(word[0]+word[-1])

#실습2
value="""이것은 사과입니다. This is an apple.
이것은 애플입니다. This is an Apple."""
#위의 문자열에서, 줄바꿈이 몇번째 인덱스에 있는지를 출력하세요.

#답2-1
print(value.index("\n"))


#실습3
value1="3.141592"
value2="192.168.5"
#위 두 문자열을 합친 결과물이 정수형변환이 되도록 불필요한 문자를 제거하고
#형변환된 정수값을 2로 나눈 몫을 출력하세요.

#답3-1
value1=value1.replace(".","")
value2=value2.replace(".","")
value3=int(value1+value2)
print(value3//2)

#답 3-2
result=value1+value2
result=result.replace(".","")
result=int(result)
print(result//2)



