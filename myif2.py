def print_cat():
        print(line)


        for line in cat:
            print(line)

      # 아스키 코드 그림 출력 하기
def print_cat():
    cat = [
        " /\\_/\\  ",
        "( o.o ) ",
        " > ^ <  "
    ]
    for line in cat:
        print(line)

def print_dog():
    dog = [
        " / \\__",
        "(    @\\___",
        " /         O",
        "/   (_____/ ",
        "/_____/   U"
    ]
    for line in dog:
        print(line)

def print_rabbit():
    rabbit = [
        "  (\\_/)",
        "  (o o)",
        "  ( > )"
    ]
    for line in rabbit:
        print(line)

#  반복 5번
for i in range(5):
    print("\n그림 출력 프로그램")
    print("=====================")
    print("1. 고양이")
    print("2. 강아지")
    print("3. 토끼")
    print("=====================")
    n = input("선택: ")

    if n == "고양이":
        print("고양이 그림")
        print_cat()
    elif n == "강아지":
        print("강아지 그림")
        print_dog()
    elif n == "토끼":
        print("토끼 그림")
        print_rabbit()
    else:
        print("잘못 입력")
      
 # 무한 반복
while True:
    print("\n그림 출력 프로그램")
    print("=====================")
    print("0. 종료")
    print("1. 고양이")
    print("2. 강아지")
    print("3. 토끼")
    print("=====================")
    n = input("선택: ")

    if n == "0":
        print("프로그램을 종료합니다.")
        break
    elif n == "고양이":
        print("고양이 그림")
        print_cat()
    elif n == "강아지":
        print("강아지 그림")
        print_dog()
    elif n == "토끼":
        print("토끼 그림")
        print_rabbit()
    else:
        print("잘못 입력했습니다.")