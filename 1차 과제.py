def calculate_flow_rate():
    print("유량 계산기에 오신 것을 환영합니다!")
    while True:
        print("\n다음 중 계산하고자 하는 유량을 선택하세요:")
        print("1. 유속과 단면적으로 유량 계산")
        print("2. 유량과 단면적으로 유속 계산")
        print("3. 종료")

        choice = input("선택 (1/2/3): ")

        if choice == '1':
            velocity = float(input("유속을 미터/초 단위로 입력하세요: "))
            area = float(input("단면적을 제곱미터 단위로 입력하세요: "))
            flow_rate = velocity * area
            print("유량은 {} 입니다.".format(flow_rate))
        elif choice == '2':
            flow_rate = float(input("유량을 입방미터/초 단위로 입력하세요: "))
            area = float(input("단면적을 제곱미터 단위로 입력하세요: "))
            velocity = flow_rate / area
            print("유속은 {} 미터/초 입니다.".format(velocity))
        elif choice == '3':
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 옵션을 선택하세요.")


calculate_flow_rate()