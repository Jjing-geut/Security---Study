#1. 기억해!(변수)
'''
변수 -> 데이터 상자
[변수이름] = 데이터
=은 '대입'이라는 개념으로 생각하기
'''
fruit1 = input("좋아하는 과일을 입력하시오 : ")
print(fruit1)

name = "마리오"
print(name)

#2. 데이터 타입
'''
* 데이터에는 여러 종류(타입)이 있다. 따라서 1+1은 숫자들의 합이 아닌 문자열들의 연결이기 때문에 '2'가 아닌 '11'로 나옴

+ 기호는 더하기가 아닌 연결!(문자열의 경우에는)
'''

num1 = input("숫자를 입력해주세요 : ")
num2 = input("숫자를 입력해주세요 : ")

print(num1+num2)

#3. 숫자 데이터
'''
숫자 데이터 사용하는 방법 : 따옴표를 사용하지않고 그냥 입력하면 숫자로 인식하여 숫자끼리 더하는게 가능해짐
num1 = 1
num = 5

* 데이터의 유형을 알고싶다면 type() 함수를 통해 알 수 있음(int, str, float, bool 등등)
* 지금 내가 쓰고 있는 변수는 어떤 데이터 유형인지 확인하는 과정을 자주해야함 ---> type()함수를 통해 확인 가능(출력하고싶은면 print())
* 만약 문자열과 숫자를 더한다면 지원하지 않는 오퍼랜드(연산)이기 때문에 오류가 난다.
'''

num1 = 1
num2 = 4
print(num1 + num2)

data1 = 5
print(type(data1))


#4. 참 혹은 거짓 BOOLEAN
'''
BOOL : Boolean
* 불린이란?: 참과 거짓을 표현하는 데이터 타입을 말함. 즉, True와 False 이 두가지 데이터만 가질 수 있는 데이터 타입이 바로 BOOL 타입이다.
* Boolean값은 그 자체로 데이터이기때문에 변수 설정 시 따옴표를 사용하지 않음

* 왜 사용하냐? : 두 개의 값이 같은지 비교를 위해 많이 사용함, 이때 [==] 라는 비교연산을 이용!
data1 = 1
data2 = 1
print(data1 == data2) : 야 이거 값이 같아?  ---> 결과는? : True로 나옴(다르다면 False로 나옴)
'''

data1 = True
print(type(data1))

data2 = True  # True는 1, False는 0과 같다.
data3 = 2

print(data2 + data3)

print(data2 == data3)

#5. 데이터 정리왕!(리스트)
'''
* LIST : 데이터 보관하는 장바구니, [] 를 이용함
* data = [1, "nomaltic", "사과"] --> ,로 구분지어줌
* list 안에 있는 데이터 중 두 번째 데이터를 가져오고 싶다 --> print(data[1])

1) 리스트 안에 데이터 추가하는 법 : 변수를 만들고 input()함수를 통해 데이터를 받은 후 리스트명.append(해당변수) 또는 리스트명.append(추가할 데이터)
   데이터가 추가됨
2) 리스트에 있는 데이터 삭제하는 법 : data.remove(해당 데이터)입력 또는 리스트명[번호]로 지울 수 있음
3) 리스트에 있는 데이터를 다른 데이터로 바꾸는 법 : data[번호] = "변환할 데이터"
4) 리스트에 있는 데이터 개수 확인하는 법 : len()함수를 통해 변수 이름을 입력하고 print()출력하면 알 수 있음  ---> print(len(data))
'''

#cf) tuple
'''
* 리스트와 비슷하지만 []가 아닌 ()를 사용한다. --> datalist = (1,2,4)
* 하지만 내부의 값을 변경하거나 삭제할 수 없다.
'''

#6. 정리킹왕(Dictionary)
"""
* key-value 형태로 이루어짐(좀 더 직관적으로 알 수 있음, 코드의 가독성을 높임)
* data = {"name":"mario", "fruit":"apple"} -> ,로 구분지어줌(중괄호 사용)
* 변수 안에 있는 데이터를 가져오고 싶다 -> print(data["name"])

1) Dictionary 안에 데이터 추가하는 법 : 새로운 키 값과 밸류값을 추가함 -> data["animal"] = "monkey"
2) Dictionary 안에 데이터 삭제하는 법 : del()함수를 이용 -> del(data["name"])
3) Dictionary 안에 데이터 다른 데이터로 바꾸는 법 : 밸류값을 바꿈 -> data["name"] = "시노준"
"""

#7. 띄어쓰기 잘해라? | 조건문과 Indent
"""
* 언제 사용하냐? :  "이러이러한 상황일 때 이 코드가 실행되면 좋겠어!"
* 사용법 : if문을 만들고 밑에 코드를 만들면 됨 -> if():
이때 콜론을 쓰고 enter를 누르면 들여쓰기(indent)가 생김
* indent란 'if문 안에 있는 조건이 맞으면 실행됐으면 좋겠어'라는 코드블럭이다.(C언어의 {}임) -> 즉 indent안에 있는 코드와 그렇지 않는 코드를 구분해줌
* <주의> : tab을 이용하여 indent를 넣을 수 있지만, 반드시 구문의 indent를 통일시켜줘야함
* cf) if문 안에 있는 조건문은 사실 Boolean값임
"""

num1 = 100

if(num1 > 0):
    print("조건문이 실행됨!")

print("이거는 indent 없으니까 다른 코드로 생각해라~")

# 만약 num1이라는 변수값을 0으로 바꾼다면 조건문은 거짓이 되므로 밑에있는 코드만 실행된다!


#8. 만약에 말이야.. | 조건문(elif와 else)
"""
* else : if문 외의 경우, 즉 if문이 실행되지 않으면 실행될 코드(else 뒤에는 조건, 즉 Boolean값이 오지 않음)
- if문을 두 번 쓰기보단 else를 사용할 수 있음

* elif : if문이 거짓이라면 else가 아닌 elif문을 확인함
- 우선순위를 두자면 if > elif > else 
"""
num1 = 100
num2 = 50

if(num1 > num2):
    print("num1이 더 커요!")
elif(num1 == num2):
    print("num1과 num2가 같아요!")
else:
    print("num1이 더 작아요!")
 
 #9. 예외 처리
"""
 * 프로그래밍 시 입력값을 제대로 입력하지 않는 등의 오류를 일으키는 예외의 상황이 일어날 수 있기 떄문에 이를 해결해야함
 * 해결책 및 형태 : try 와 except를 이용한다.
try:
    (예외가 일어날 수 있는 코드)
except:
    (예외가 일어났을 때 실행하는 코드)

* 하지만 변수를 통해 입력값을 받는 코드의 경우, try구문 안에 해당 변수를 넣고 except구문을 통해 예외처리를 하였을 해당 변수가 정의되어 있지 않기
  때문에 오류가 발생한다. 
  해결책 -> 아예 try구문 안에 코드 전체를 넣어서 실행하거나, except구문에 exit()함수를 이용하여 문자 입력 시 프로그램을 종료시킨다.
"""
try:
    score = int(input("점수를 입력해주세요 : "))
except:
    print("점수는 숫자를 입력해줘야 합니다.")
    exit()

if(score == 100):
    print("잘했어요~")
elif(score < 100 and score >= 80):
    print("괜찮아요~")
elif(score < 80 and score >= 40):
    print("노력해요~")
elif(score < 40 and score >= 0):
    print("공부 안 했니?")
else:
    print("제대로된 점수를 입력해주세요.")
#이렇게 할 수도 있고 또는!
try:
    score = int(input("점수를 입력해주세요 : "))
    if(score == 100):
        print("잘했어요~")
    elif(score < 100 and score >= 80):
        print("괜찮아요~")
    elif(score < 80 and score >= 40):
        print("노력해요~")
    elif(score < 40 and score >= 0):
        print("공부 안 했니?")
    else:
        print("제대로된 점수를 입력해주세요.")
except:
    print("점수는 숫자를 입력해줘야 합니다.")
# 구문 속에 indent 잘 구분하자~!


#10. 계속해! 언제까지? | 반복문 while
"""
* 똑같은 코드를 반복해서 사용하고 싶을 때 OR
  어떠한 조건이 만족될 때까지 입력을 받고 싶을 때 등에 사용!
-형태
while(조건):
    print("안녕~~!")

* 반복문인 while()함수는 참인 조건에서 계속 실행됨. cf) while(True)는 무한루프임!
  따라서 While문을 끝내기 위해서는 조건을 잘 적어줘야 함.
-> 이때 break를 이용!
"""
num = int(input("숫자를 입력해주세요 : "))

while(True):
    num = int(input("숫자를 입력해주세요 : "))
    if(num == 0):
        break

print("당신이 입력한 숫자는 " + str(num) + " 입니다.")


#11. 영원한 굴레 탈출하기 | 무한루프 다루기
"""
cf) while문에 조건을 True로 하면 무한루프를 할 수 있으며
밑에 if문 등의 조건을 적고 break 코드로 탈출하는 코드들을
해커들은 자주 이용함

* 'break'는 현재 반복문을 빠져나오고 싶을 때 사용한다.

* 'continue"는 현재 반복문에서 실행되고 있는 코드중에 continue까지만
  실행하고, 다시 while 문의 조건을 판단하는 곳으로 올라가게 한다.
  즉, continue 아래 있는 반복문 코드들은 실행되지 않는다.
"""
while(True):
    num = int(input("숫자를 입력해주세요 : "))

    if(num > 100):
        break
    if(num == 50):
        print("Half??")
        continue          #숫자가 50일 때는 Oh~ No~~는 출력되지 않고 Half??만 출력하고 싶을 때!!!!
    print("Oh~ No~~~")

print("당신이 입력한 숫자는 " + str(num) + " 입니다.")


#12. 여기있는 애들 다 주세요 | 반복문 for
"""
* for문의 특징 : list에 있는 데이터를 다룰 때 while문의 경우 따로 변수를 넣어야하지만 for문은 이를 쉽게 해결가능!
* 문법 : for (for문 안에서 사용할 변수) in (list):
"""
# while문을 이용하여 list에 있는 데이터를 출력하는 법(변수 사용)
datalist = ["Chicken", "Pizza", "Hambuger", "Hotdog"]
num = 0

while(num < len(datalist)):
    print(datalist[num])
    num = num + 1

# for문을 이용하여 list에 있는 데이터를 출력하는 법
datalist = ["Chicken", "Pizza", "Hambuger", "Hotdog"]

for food in datalist:
    print(food)


#13. 1000까지!!! | for Range
"""
만약 for문을 이용하여 1부터 100까지의 숫자를 출력하고싶다면 list에 1부터 100까지의 데이터를 입력해줘야 할 것이다.(따흐흑...)
* 하지만 range를 이용한다면 쉽게 해결 가능!
* 사용법
1. 리스트에 range를 이용하거나  -> numlist = range(1, 101)
2. for문에 바로 사용하거나  -> for num in range(1,101):   -> list를 만들 필요가 없어짐!
                                 print("num")         
* range를 이용하여 범위를 지정할 때는 해당 횟수까지의 수에 1을 더하여 이용한다.
"""
numlist = range(1,11)

for num in numlist:  # numlist를 바로 range(1,11)로 쓸 수 있음(list 만드는 수고를 덜을 수 있다.)
    print(num)       # num을 Hello로 바꾼다면 Hello가 10번 반복되는 반복문이 만들어진다.
                     # *for문은 in 뒤에 있는 리스트의 데이터 또는 range의 범위만큼 반복된다.


#14. Function | 함수 개념(Function = 자판기)
"""
function을 쓰는 이유? 
1) 코드를 반복해서 쓰지 않기 위해
2) 코드 가독성!
3) 다른사람들의 함수를 내가 사용하거나 내가 만든 함수를 다른사람들이 사용할 수 있도록

*사용법 : 함수이름(전달하고싶은 데이터)  -> 전달하고싶은 데이터 ≒ 인자(전달인자) ≒ argument 

cf) argument vs parameter
argument는 함수로 전달하는 데이터
parameter 함수에서 정의한 매개변수 즉, 함수 안에서 사용되는 (전달된) 변수

ex)
def test(name, age):
    print(name, age)

test("normaltic", 10)

name과 age는 파라미터, 
normaltic과 10 은 argument!
"""


#15. 나도 마법의 단어를! | 함수 만들기
"""
* 파이썬에서 함수 만드는 법 : def 함수이름(전달받을 인자):
                              (필요한 코드들)
"""
# 간단한 계산기 만들기!
def calc(num1, num2):
    print(num1+num2)

calc(23, 45)
# return을 통해 입력뿐만 아니라 출력의 개념까지 이용하기!(입력받은 데이터를 다른 곳에서 받아볼 수 있음)
def calc(num1, num2):
    res = num1 + num2
    return res         # num1+num2의 결과인 res라는 변수를 return 받은 상태

result = calc(23, 45)   # 위의 return받은 결과를 result라는 변수를 통해 받아야함!

print(result)

# 내가 만든 함수!
def calc(a, b):
    print("{}와(과) {}를(을) 입력받았습니다.".format(a, b))
    print("두 값을 더하면 {}입니다.".format(a+b))

    res = a+b
    return res

result = calc(10,30)

print("[*****]계산기 스니핑 작동!")
print("계산 결과는 {}이다. 맞지?ㅋㅋ".format(result))


#16. 다른 사람들 땡큐! | Library, Module
"""
* 형태 : import 라이브러리 이름  -> 구글링을 통해 라이브러리 검색 가능!
* 간혹 어떤 모듈(라이브러리)들은 준비가 되어있지 않음 -> 해결책 : pip install 모듈 이름
* 라이브러리 이름이 너무 길어 귀찮다면?  -> 해결책 : as 지정이름(ex. import random as r)
"""
import random   # 아하! random이라는 라이브러리가 있구나
print(random.randrange(1,10))  # 아~ random이라는 라이브러리 안에는 randrange라는 함수가 있구나!

import requests
# 모듈이 설치가 안되어있다? -> [*] pip install requests

import random as r


