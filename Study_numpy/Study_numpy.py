from curses.ascii import isdigit
import numpy as np
from Study_numpy_fucntions import Functions
from Study_numpy_fucntions import User_Choic_Content

SYSTEM_LOG = "시스템 - "

def check_input_int():
     while True:
          x = input(SYSTEM_LOG+"선택해주세요. : ")
          if x.isdigit(): 
               user_input = int(x)
               if isinstance(user_input,int):
                    if user_input>=0  and user_input<=5 : return user_input
          else: print("입력 값이 올바르지 못합니다. 다시입력해주세요.")
          
def user_choice_notice(value):
     temp = ""
     if value == 1: temp = User_Choic_Content.numpy_Array.value
     elif value == 2: temp = User_Choic_Content.numpy_Array_Chaing.value
     elif value == 3: temp = User_Choic_Content.numpy_Statistics.value
     elif value == 4: temp = User_Choic_Content.numpy_RandomCount.value
     elif value == 5: temp = User_Choic_Content.exit.value
     print(temp + "를(을) 실행합니다.")

np_title = "{:*^100}".format(" NUMPY TUTORIAL ")
print(np_title)
np_intro =     """
               import numpy as np\n
               왜 리스트를 사용하지 않고 넘파이를 이용하는가?\n
               넘파이는 모든 원소가 같은 자료자료형이고 C로 내부를 구현해 속도가 빠르다.\n
               <입력> (숫자만 입력해주세요.)\n
               1. 넘파일 배열 만들기 과정\n
               2. 넘파일 배열 변경 과정\n
               3. 통계 관련 기술\n
               4. 난수 관련 기술
               5. 종료
               """
print("{:^100}".format(np_intro))
print("{:*^100}".format(""))
system_input_data = check_input_int()
user_choice_notice(value=system_input_data)
Functions(system_input_data)