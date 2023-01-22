#복습문제
#두개의 실수를 입력을 받아 저장합니다.
#입력받은 두 실수 중 첫번째를 두번째로 나눈 값(A값)을 저장합니다.
#A값에 대하여 소수점 2자리까지 반올림처리하여 (-> 일반포맷팅)
#다시 실수값(B값)으로 준비합니다. (->포맷팅 결과를 형변환처리)
#B값에서 A값을 빼면 반올림이 된 만큼 오차가 발생하고,
#그 오차를 소수점 10자리까지 출력하세요. (->일반 포맷팅으로 출력)

#단축키 팁 : ctrl + d -> 드래그한 대상과 같은 것에 커서 잡기

#답
fnum1=float(input("실수1 입력 :"))
fnum2=float(input("실수2 입력 :"))

#답1
resultA=fnum1/fnum2
print("A값 :",resultA)
resultB=float("%.2f"%(resultA))
print("B값 :",resultB)
resultC=resultB-resultA
print("오차 :%.10f"%(resultC))

#답2
Avalue=fnum1/fnum2
Bvalue=float("%.2f"%(Avalue))
print("오차 : %.10f"%(Bvalue-Avalue))
