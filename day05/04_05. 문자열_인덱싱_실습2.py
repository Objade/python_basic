#print()의 옵션으로 2가지가 존재함
#(바꿀 필요가 있을 때에만 추가하자)
#sep : separator의 약자, 구분자가 사용되었을 때, 이를 다른 것으로 바꿀 수 있음
#end : print의 기본 줄바꿈을 바꿀 수 있음
#둘의 순서는 딱히 상관 없음

word="HLEO! WRD"
print(word[0]+word[2]+word[1]*2+word[3], sep="")
print(word[0],word[2],word[1]*2,word[3], sep="#") #기본 띄어쓰기를 바꿀 수 있음

print(word[0]+word[2]+word[1]+word[1]+word[3], end=" ") #print의 기본 줄바꿈을 바꿀 수 있음
print(word[-3]+word[3]+word[-2]+word[1]+word[-1]) 
