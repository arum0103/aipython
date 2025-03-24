#number = int(input("출력할 구구단 숫자를 입력하세요: "))
s_number = input("출력할 구구단 숫자를 입력하세요 (예: 2): ")
print(f"(number)단:")
#print(number, "단:")
#print(number + "단:")
#print(f"(number)단, (number)단, (number)단") 
# number 값이 문자열이기 때문에 숫자로 변경해서 연산
number = int(s_number) #문자숫자가 숫자로
result = number * 2
print(result)