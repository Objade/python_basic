# input : 키보드로 입력받은 값을 사용된 곳에 바꿔치기로 준비해줌

word="APPLE, LION, CANDY"
#주의사항 1 : 반드시 안내문자열을 작성해야 함
value=input("아무거나 입력 >> ") #안내사항을 입력해주기! 고객의 편의를 위함

#-> 소스파일은 소중한 것이고, 특별한 경우가 아니면 오픈하지 않는다.
#-> 관련자가 아니면 소스파일을 읽지 못한다.
#-> 프로그램 사용자는 오로지 화면에 나오는 내용에만 의존하게 된다.

print("결과 : ", value in word)
