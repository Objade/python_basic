#인덱싱 : 인덱싱 할 수 있는 것들에 대해서 전체가 아닌, 일부만 가져와서 쓰겠다.
#왜? 전체가 필요가 없으니까.

idn="010203-3234567" #주민등록번호
print(idn)
print("성별 :", idn[-7])
print("태어난 연도 :", "20"+idn[0]+idn[1])
print("태어난 월 :",idn[2]+idn[3])
print("태어난 일 :",idn[4]+idn[5])

#인덱싱 주의사항 : 인덱스 번호를 넘어서면 에러가 발생한다
#print(idn[20]) (IndexError : 인덱스 번호가 존재하지 않음)
#print(idn[-16]) (없으면 못씀)

#팁1 : 전체 글자수-1 = 정방향 인덱스 마지막
#      - 전제 글자수 = 역방향 인덱스 마지막
#     len() 이용하면, 마지막 인덱스를 금방 구할 수 있음

#팁2  : 억지로 인덱스 번호를 체크할 필요 없이, 대충 찍어서 확인하면 됨

word="ABCDEFG" #정방향 : 0123456 / #역방향 : -7654321
num=len(word)
print(num-1, -num)


#실습문제1

word="HLEO! WRD"
print(word[0]+word[2]+word[1]+word[1]+word[3]+word[5]
      +word[-3]+word[3]+word[-2]+word[1]+word[-1])
