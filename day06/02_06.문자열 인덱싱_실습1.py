#실습예제2

#답2-1

address=input("주소 입력 :")
print("시 :", address[:3]) 
print("구 :", address[4:7])
print("동 :", address[-3:])

#실제로는 이와 같은 방식으로 잘 쓰이지는 않음
#->무조건 원하는/필요한 형식으로 맞춰진 값만 준비가 되어야 함
#상수값으로 슬라이싱을 운용하게 되면 융통성이 심하게 떨어짐


#실습예제3

#답3-1
word="Pyon Simple"
value1="th"
value2="is"
print(word[:2]+value1+word[2:4], value2, word[-6:])

#답3-2
word="Pyon Simple"
value1="th"
value2="is"
print(word[:2]+value1+word[2:5]+value2+word[-7:])

#답3-3
word="Pyon Simple"
print(word[:2]+"th"+word[2:5]+"is"+word[4:])

#실습예제4

#답4-1 #좀 더 눈에 잘 들어옴
word="국민은행 123-444555 100만원 입금"
print("은행 :", word[:4])
print("계좌 :", word[5:15])
print("금액 :", word[16:21])

#답4-2 #코드를 한 줄로 만들 수 있음
word="국민은행 123-444555 100만원 입금"
print("은행 :", word[:4],"\n계좌 :",word[5:15],"\n금액 :", word[16:21])

#답4-3 #sep를 사용해도 됨
word="국민은행 123-444555 100만원 입금"
print("은행 : "+word[:4],"계좌 : "+word[5:15],"금액 : "+word[16:21], sep="\n")
