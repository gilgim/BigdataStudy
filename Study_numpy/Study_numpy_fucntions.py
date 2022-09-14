import numpy as np
from enum import Enum

class User_Choic_Content(Enum):
     numpy_Array = "Create array with numpy"
     numpy_Array_Chaing = "넘파일 배열 변경"
     numpy_Statistics = "통계 관련 기술"
     numpy_RandomCount = "난수 관련 기술"
     exit = "종료"

class Functions(object):
     def __init__(self, user_choice):
          self.user_choice = user_choice
          if self.user_choice == 1 : 
               self.number_1()

     def number_1(self):
          intro =   """
                    다음과 같은 기능을 확인 할 수 있습니다.\n
                    1차원 배열 만들기\n
                    for문을 사용하지 않는 원소 연산\n
                    다차원 배열 만들기\n
                    원소 입출력
                    """
          print_intro(title=User_Choic_Content.numpy_Array.value, intro=intro)

def print_intro(title,intro):
     print("{:*^100}".format(" %s " % title))
     print("{^100}".format(intro))
     print("{:*^100}".format(""))