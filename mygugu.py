# 숫자 두개를 입력을 받아서
# +, -, *, / 를 출력하는 프로그램을 만들어 보자
while True:
    try:
        num1 = float(input("첫 번째 숫자를 입력하세요: "))
        num2 = float(input("두 번째 숫자를 입력하세요: "))
        break  # 숫자가 정상적으로 입력되면 루프 탈출
    except ValueError:
        print("숫자만 입력하세요!")  # 숫자가 아닐 경우 다시 입력 요청

print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")

# 0으로 나누는 경우 예외 처리
if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
else:
        print("0으로 나눌 수 없습니다.")
