import matplotlib.pyplot as plt

from open_data import housing
from divide_data import dividing
from divide_data import sampling_strat

#첫 실행 시 데이터 사용 문구
DIVIDE_LINE = '=========================================================='
CREAT_TEXT = ('Creat meant adding new category to orginal housing data.'
               '\nIf you want to use orginal data, you should input \'n\''
               '\nBut you want to divid data, you should input\'y\'')

#명령어 문구    
COMEND_LIST = ('The following functions are available for the current system:'
               '\n-> head / info / describe / graph / stratified / exit')
def is_contain_value(category_value):
     is_success = False

     for x in list(housing):
          if x == category_value:
               is_success = True
               break
     return is_success

def check_data():
     while True:
          print('\n'+DIVIDE_LINE+'\n'+COMEND_LIST+'\n'+DIVIDE_LINE)
          input_value = input("Please input action. : ")
          print('\n')

          if input_value == 'head':
               print(housing.head())
          elif input_value == 'info':
               print(housing.info())
          elif input_value == 'describe':
               print(housing.describe())
          elif input_value == 'v_count':
               while True:
                    category_input = input('Please input data category. : ')
                    is_success = is_contain_value(category_value=category_input)
                    if is_success:
                         print(housing[category_input].value_counts())
                         break
                    elif is_success == False:
                         print('It is not housing configuration')
          elif input_value == 'graph':
               graph_kind = input('Do you want to see All data? y/n : ')
               while True :
                    if graph_kind == 'y':
                         housing.hist(bins=50,figsize=(20,15))
                         plt.title("house_data")
                         plt.show()
                         break
                    elif graph_kind == 'n':
                         category_input = input('Please input data category. : ')
                         is_success = is_contain_value(category_value=category_input)
                         if is_success:
                              housing[category_input].hist()
                              plt.title("category_input")
                              plt.show()
                              break
                         elif is_success == False:
                              print('It is not housing configuration')
                    else:
                         print('It is not right.')
          elif input_value == 'stratified':
               if is_refresh_data == 'y':
                    sampling_strat(new_value_name=new_category_name)
          elif input_value == 'exit':
               break
          else:
               print('Error')

print('\n\n')
print(DIVIDE_LINE+'\n'+CREAT_TEXT+'\n'+DIVIDE_LINE)
while True:
     is_refresh_data = input('input : ')
     if is_refresh_data == 'y':
          while True :
               new_category_name = input('Please input new category name. : ')
               housing_category_name = input('Please input housing category name. : ')
               if is_contain_value(housing_category_name):
                    dividing(new_value_name=new_category_name,housing_ctg_name=housing_category_name)
                    print('creat complete')
                    break
               else:
                    print('it is not right value')
          break
     elif is_refresh_data == 'n':
          print('use original data')
          break
     else:
          print('it is right value.')
check_data()