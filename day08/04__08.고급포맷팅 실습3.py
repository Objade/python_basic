#포맷팅==서식
#포매팅을 이용해서 달성하는 것 
#-> 가치가 있는 것 (값 - 자료/정보)를 꾸며주는 표현과 함께 붙여 생성/사용하는 것

#실습예제 1

#답 1-1

product=input("상품 입력\t: ")
price=int(input("가격 입력\t: "))
result=input("평가 입력\t: ")

print("상품명\t: {}\n가격\t: {}\n평가\t: {}".format(product, price,result))
print("{}의 가격은 {}원이며\n현재 {}를 받고 있습니다.".format(product,price,result))

#답 1-2

product=input("상품 입력\t: ")
price=input("가격 입력\t: ")
result=input("평가 입력\t: ")

print("""상품명\t : {0}
가격\t: {1}
평가\t: {2}
{0}의 가격은 {1}원이며
현재 {2}를 받고 있습니다.""".format(product,price,result))


#실습예제 2

#답 2-1
word1=input("단어 1 입력 :")
word2=input("단어 2 입력 :")

print("{0} {1} {0} {1}\n{0} {1} {0} {1}\n{0}과 {1}의 반복입니다.".format(word1, word2))
print("{1} {0} {1} {0}\n{1} {0} {1} {0}".format(word1, word2))


#답 2-2
#반복되는 건 끔찍하다
#포매팅은 문자열에 대한 연산/기능이기 때문에 연산한 결과물에 대해서도 가능하다.
print(((("{0} {1} "*2)+"\n")*2+"""{0}과 {1}의 반복입니다."""+ (("{1} {0} "*2)+"\n")*2).format(word1, word2))



#실습예제 3

#답 3-1

shape=input("문자 입력 :")
size=int(input("크기 입력 :"))
result1=str(shape*size+"\n")*size

print("일반포매팅 큐브\n"+"%s"%(result1))
print("고급포매팅 큐브\n{}".format(result1))


# 답 3-2

# 단순 연산 큐브
print((shape*size+"\n")*size)


# 일반 포맷팅 : 위의 코드에서 어디에 적용되어야 쓸 수 있을까?
# 어떤 방법을 쓰더라도 일반포맷팅만으로는 중복처리가 불가능함
# -> 1회성으로 값이 쓰이는 형태라면, 고급보다는 쓰기 편한 경우가 많다.

print(("%s"%(shape)*size+"\n"*size))




# 고급 포맷팅 : 일반포맷팅처럼 넣을 수 있지만, 어디에 넣으면 효율적일까?
# -> 일반포맷팅처럼 사용도 가능하고, 중복처리도 가능함
# -> 1회성을 위해 쓰기에는, 더 배워야 편해짐
print((("{0}"*size+"\n")*size).format(shape))
