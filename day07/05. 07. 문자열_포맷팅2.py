#실습문제1

#서식 : 값을 넓은 시야로 봐야한다
#       -> 어떤 형태가 반복되고 있는가?

#답1
from re import A


name1=input("이름1 입력 :")
age1=input("나이1 입력 :")
hobby1=input("취미1 입력 :")
name2=input("이름2 입력 :")
age2=input("나이2 입력 :")
hobby2=input("취미2 입력 :")

print("이름\t나이\t취미")
print("%s\t%s\t%s"%(name1,age1,hobby1))
print("%s\t%s\t%s"%(name2,age2,hobby2))

#답2

name1=input("이름1 입력 :")
age1=input("나이1 입력 :")
hobby1=input("취미1 입력 :")
name2=input("이름2 입력 :")
age2=input("나이2 입력 :")
hobby2=input("취미2 입력 :")

print("이름\t나이\t취미")
print(name1,age1,hobby1, sep="\t")
print(name2,age2,hobby2, sep="\t")

#답3
form1="%s 입력 :"
form2="%s\t%s\t%s"

name1=input(form1%("이름1"))
age1=input(form1%("나이1"))
hobby1=input(form1%("취미1"))
name2=input(form1%("이름2"))
age2=input(form1%("나이2"))
hobby2=input(form1%("취미2"))

print("\n이름\t나이\t취미")
print(form2%(name1,age1,hobby1))
print(form2%(name2,age2,hobby2))


#실습예제2

#답1
num1=input(form1%("분기"))
num2=int(input(form1%("매출")))
num3=input(form1%("평가"))

print(num1,"의 매출 :",num2,"만원")
print(num1,"의 평가 :",num3)

#답2
value1=input("분기 입력 :")
value2=int(input("매출 입력:"))
value3=input("평가 입력:")

print(value1+"의 매출 :"+str(value2)+"만원\n"+value1+"의 평가 :"+value3)

#답3
value11=input("분기 입력 :")
value22=int(input("매출 입력:"))
value33=input("평가 입력:")
print("%s의 매출 : %d만원\n%s의 평가 : %s"%(value11, value22, value11, value33))

#서식 : 값만 채워주면 알아서 나옴

#요약
#포맷팅 : 서식을 만든다
#그 서식 : 이력서

