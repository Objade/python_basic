#문자열 메서드 : 특정 값에서 사용할 수 있는 전용 함수
#자주 쓰는 다섯가지 : count, index, replace, split, format
msg="This is an Apple!"

#1. count(문자열) : 문자열의 수량을 세어줌
print(msg.count("i")) #'i'의 개수는 2개 이므로 값은 2가 나옴

#1-1. 응용 : 입력된 값이 실수인지 아닌지 판단하고자 할 때
value="3.14" #문자값으로 넣어야 가능 (실수값으로는 판단하기 위해서는 str을 사용해서 형변환을 해야함)
print(value.count(".")==1) #실수라면 점이 하나뿐임 -> 실수가 맞으므로 'True' 라고 나옴

value="3.14.15"
print(value.count(".")==1) #실수가 아니므로 'False' 라고 나옴

values="ABCDEFGHIJKLMNOPQRSTUVXYZ"
print(value[0] in values) #변수에 0이 존재하지 않으므로 'False' 가 나옴

#2. index(문자열) : 문자열의 정방향 인덱스를 구해줌
print(msg.index("This"))

#2-1. 응용 : 컴퓨터가 알아낸 결과물을 이용해 슬라이싱 할 수 있음
i=msg.index(" ") #첫번째 값의 인덱스를 알아냄
word1=msg[:i] #인덱스는 변수로 대체할 수 있음
print(word1)
msg1=msg[i+1:]
print(msg1)

i=msg1.index(" ")
word2=msg1[:i]
print(word2)
msg2=msg1[i+1:]
print(msg2)

#이러한 절차를 '알고리즘' 이라고 함

#3. replace(A,B) : A를 찾아서 B로 고침
# -> 특정 문자, 특정 문자열, 특정 단어를 바꾸는 것이 목적임
print(msg)
msg=msg.replace("i","I",1) #필요하다면 바꿀 수량을 조절할 수 있음 (단, 위치는 항상 첫번째것 먼저로 고정됨)
print(msg)

print(msg)
msg=msg.replace("i","I")
print(msg)

#3-1. 응용 : 특정 불필요한 문자를 일괄삭제/문자 사이에 일괄 삽입
msg=msg.replace(" ","")
print(msg)
msg=msg.replace("","#") #이렇게는 잘 안씀.
print(msg)

#4. split() : 문자열을 쪼개서 리스트로 바꿔줌
#             -> 편하게 쓸 수 있도록 쪼개서 나눠줌
msg="This is an Apple!"
result=msg.split()
print(result)

#5. 그외의 것
#5-1. upper/lower : 영어권에서 많이 사용됨
#                   -> 소문자를 대문자로 / 대문자를 소문자로

word="John Smith"
print(word.upper())
print(word.lower())

#5.1_응용 : 영단어의 검색에 이용됨
print("Apple"=="apple")
fword="Apple"
word="apple"
print(fword.lower() == word)

#5-2. strip : 벗긴다
#-> 일정한 규칙으로 만들어진 문자열 값에서 필요한 것만 남기는 용도
#-> 인터넷 주소
iaddress="https://www.naver.com"
result=iaddress.strip("mht") #문자열 목록표를 만든다. 문자 단위로 체크.
print(result)
result=result.strip("ps:/wco")
print(result)
result=result.strip(".")
print(result)
#바깥쪽부터 진행되는 구조
#규칙성이 없는 문자값이라면 의미가 없음


