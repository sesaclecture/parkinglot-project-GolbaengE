#주차장 입·출차 시스템
from datetime import datetime

today = datetime.today()

from enum import Enum

class discount(Enum): #차량별 할인율, enum으로 역할 부여
    BASIC = 10
    LPG = 30
    ELEC = 50

exit = True # 프로그램 종료 변수

#층별 주차구역 정의
_1f = [
    [None, None, None, None, None],
    [None, None, None, None, None]
    ]
_2f = [
    [None, None, None, None, None],
    [None, None, None, None, None]
    ]
_3f = [
    [None, None, None, None, None],
    [None, None, None, None, None]
    ]
_4f = [
    [None, None, None, None, None],
    [None, None, None, None, None]
    ]
_5f = [
    [None, None, None, None, None],
    [None, None, None, None, None]
    ]

#입출차 유저 정의
users = {
    "2245" : {
        "numbers" : "2245",
        "regular_parking" : True, # 정기권 여부
        "entry_time" : "",
        "exit_time" : "",
        "parking_floor" : "",
        "parking_spot" : "",
        "discount" : discount.BASIC.value # 할인율
    },
    "9942" : {
        "numbers" : "9942",
        "regular_parking" : True,
        "entry_time" : "",
        "exit_time" : "",
        "parking_floor" : "",
        "parking_spot" : "",
        "discount" : discount.LPG.value
    }
}

discount_users = {
    "2245", "9942"
}

#요금 정의
parking_fee = 100 # 1시간에 6천원, 10분에 1000원
display = [_1f, _2f, _3f, _4f, _5f]
floor = 1
while exit:
    for floor, d_a in enumerate(display, start=1): #display 변수를 나열 / 첫째줄 -> [[None, 'X', None, None, None], [None, None, None, None, 'X']]
        print('='*3+f"{floor}F"+'='*3) # 결과값 ==={floor}F=== / 층별 나누기
        for d_b in d_a: #d_b변수로 d_a 변수를 차례대로 나열 할 때 / 첫째줄-> [None, 'X', None, None, None]
            for d_c in d_b: #c_f 변수로 _d_1f 변수를 차례대로 나열할 때 첫째줄 -> None
                symbol = d_c if d_c else "" #symbol 변수는 d_c가 값이 있을 때 d_c, 아니면 빈칸
                print(f"[{symbol:^3}]", end = " ")#symbol 변수값을 가운데, 3칸 띄워서 넣어라, 종료후 빈칸이 아닌 띄워쓰기
            print() #줄바꿈
        floor += 1 #층바꿈 
    print("==="*20)
    print("안녕하세요 피톤치드 주차타워입니다")
    print("입/출차를 원하시면 아래에 숫자를 입력하세요")
    print("입차 ( 1 ) / 출차 ( 2 ) / 종료 ( 3 )")
    roby = input("입력 : ")
    print("==="*20)
    if roby == "1": #입차 시
        exit2 = True
        while exit2:
            print("차량번호 4자리를 입력해주세요")
            print("예) 차량번호가 123도 1234라면 → 1234")
            numbers = input("차량번호 : ") #차량번호 입력
            if len(numbers) != 4: #차량번호 4자리가 아닐 경우
                print("==="*20)
                print("잘못 입력하셨습니다")
                print("==="*20)
                wrong = input("계속하시려면 아무키나 누르세요")
                print("==="*20)
            elif numbers in users and users[numbers]["entry_time"] != "": #이미 해당 차량이 입차 되어 있을 경우
                print("==="*20)
                print("이미 입차된 차량입니다")
                print("==="*20)
                wrong = input("계속하시려면 아무키나 누르세요")
                print("==="*20)
            else:
                exit2 = False
                exit3 = True
                while exit3:
                    print("입차시간을 입력해주세요")
                    print("예) 12시 45분이라면 → 12:45")
                    et = input("입차시간 : ")
                    try:
                        dt= datetime.strptime(et, "%H:%M")
                        exit3 = False
                    except ValueError:
                        print("==="*20)
                        print("잘못 입력하셨습니다")
                        print("==="*20)
                        wrong = input("계속하시려면 아무키나 누르세요")
                        print("==="*20)
                date_string = today.strftime("%m:%d:")
                entry_time = date_string + et
                exit4 = True
                while exit4:
                    sp = 0
                    if not None in sum(display[sp],[]):
                        sp += 1
                    print('='*3+f"{sp+1}F"+'='*3)
                    for c1 in display[sp]:
                        for c2 in c1:
                            symbol1 = c2 if c2 else ""
                            print(f"[{symbol1:^3}]", end = " ")
                        print()
                    print("원하시는 주차 위치를 입력해주세요")
                    print("ex) 1~10")
                    parking_spot = int(input())
                    sp1 = parking_spot if parking_spot <=5 else parking_spot-5
                    sp2 = 0 if parking_spot <=5 else 1
                    if 0<parking_spot<11:
                        if display[sp][sp2][sp1-1] is None:
                            print("주차 가능합니다.")
                            exit4 = False
                        else:
                            print("주차불가합니다.")

                    else:
                        print("==="*20)
                        print("잘못 입력하셨습니다")
                        print("==="*20)
                    if numbers in users:
                        users[numbers]["entry_time"] = entry_time
                        users[numbers]["parking_floor"] = f"{sp+1}F"
                        users[numbers]["parking_spot"] = parking_spot
                        display[sp][sp2][sp1-1] = "X"
                        exit = True
                    else:
                        users.update({numbers : {
                            "numbers" : numbers,
                            "regular_parking" : False,
                            "entry_time" : entry_time,
                            "exit_time" : "",
                            "parking_floor" : "sp+1",
                            "parking_spot" : parking_spot,
                            "discount" : ""
                        }   
                        })
                        exit = True
    elif roby == "2":
        exit5 = True
        while exit5:

            plate_number = input("차량번호를 입력해주세요 : ")
            if not plate_number in users:
                if len(numbers) != 4: #차량번호 4자리가 아닐 경우
                    print("==="*20)
                    print("잘못 입력하셨습니다")
                    print("==="*20)
                    wrong = input("계속하시려면 아무키나 누르세요")
                    print("==="*20)
                elif users[numbers]["entry_time"] == "":
                    print("==="*20)
                    print("없는 차량입니다")
                    print("==="*20)
                    wrong = input("계속하시려면 아무키나 누르세요")
                    print("==="*20)
            else:
                exit5 = False
                exit6 = True
                while exit6:
                    print("출차시간을 입력해주세요")
                    print("예) 12시 45분이라면 → 12:45")
                    et1 = input("출차시간 : ")
                    try:
                        dt= datetime.strptime(et1, "%H:%M")
                        exit6 = False
                    except ValueError:
                        print("==="*20)
                        print("잘못 입력하셨습니다")
                        print("==="*20)
                        wrong = input("계속하시려면 아무키나 누르세요")
                        print("==="*20)
                date_string1 = today.strftime("%m:%d:")
                exit_time = date_string1 + et1
                time1 = dt.strptime(users[plate_number]["entry_time"], "%m:%d:%H:%M")
                time2 = dt.strptime(exit_time, "%m:%d:%H:%M")
                time_difference = (time2 - time1).total_seconds() / 60
                fee = time_difference * parking_fee
                if plate_number in discount_users:
                    disc = users[plate_number]["discount"]
                    fee1 = disc /100
                    fee -= fee1
                print("==="*7+"영수증"+"==="*7)
                print(f"{plate_number} 피톤치트 주차장 이용내역")
                print(f"총 {int(time_difference)}분 사용")
                if plate_number in discount_users:
                    print(f"할인율 {disc}% 적용")
                print(f"합계 : {int(fee)}원")
                display[sp][sp2][sp1-1] = ""
                wrong = input("계속하시려면 아무키나 누르세요")
                exit = True

                
                
    elif roby == "3":
        exit1 = True
        while exit1:
            exit_1 = input("정말로 종료하겠습니까? (Y/N) : ")
            if exit_1 == "Y":
                exit1 = False
                exit = False
            elif exit_1 == "N":
                exit1 = False
            else :
                print("==="*20)
                print("잘못된 입력입니다.")
                print("==="*20)
                wrong = input("계속하시려면 아무키나 누르세요")
                print("==="*20)
    else:
        print("==="*20)
        print("잘못된 입력입니다.")
        print("==="*20)
        wrong = input("계속하시려면 아무키나 누르세요")
        print("==="*20)
        continue