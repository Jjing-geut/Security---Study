#<미션 1> - 입출력, 변수, 데이터 타입
UserData = input("이름을 말씀해주세요 : ")
print("안녕하세요~! 좋은 아침입니다! " + UserData + "님!")
print("저는 과일 좋아하는데!")
UserFruit = input("좋아하는 과일 있으세요? : ")
print("아하~ " + UserFruit + "라는 과일을 좋아하신군요!")
print("제가 바로 " + UserFruit + " 준비해드리겠습니다.")



#<미션 2> - 리스트
UserInfo = []
addData = input("이름을 말씀해주세요 : ")
UserInfo.append(addData)
print("안녕하세요~! 좋은 아침입니다! " + UserInfo[0] + "님!")
print("저는 과일 좋아하는데!")
addFruit = input("좋아하는 과일 있으세요? : ")
UserInfo.append(addFruit)
print("아하~ " + UserInfo[1] + "라는 과일을 좋아하신군요!")
print("제가 바로 " + UserInfo[1] + "준비해드리겠습니다.")
# UserInof.append(UserInfo[번호]) - 이런것도 되더라~


#<미션 3> - Dictionary
UserInfo = {}
UserInfo["name"] = input("이름을 말씀해주세요 : ")
print("안녕하세요~! 좋은 아침입니다! " + UserInfo["name"] + "님!")
print("저는 과일 좋아하는데!")
UserInfo["fruit"] = input("좋아하는 과일 있으세요? : ")
print("아하~ " + UserInfo["fruit"] + "라는 과일을 좋아하시는군요!")
print("제가 바로 " + UserInfo["fruit"] + "준비해드리겠습니다!")

print(UserInfo)
