from ast import Or
import matplotlib.pyplot as plt
import pandas as pd
from open_data import housing
from divide_data import dividing
from divide_data import sampling_strat
from pandas.plotting import scatter_matrix
#첫 실행 시 데이터 사용 문구
DIVIDE_LINE = '=========================================================='
CREAT_TEXT = ('Creat meant adding new category to orginal housing data.'
               '\nIf you want to use orginal data, you should input \'n\''
               '\nBut you want to divid data, you should input\'y\'')

#명령어 문구    
COMEND_LIST = ('The following functions are available for the current system:'
               '\n-> head / info / describe / graph / stratified / correlation /refresh / exit')
def is_contain_value(category_value):
     is_success = False

     for x in list(housing):
          if x == category_value:
               is_success = True
               break
     return is_success

def check_data():
     global housing
     first_housing = housing
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
               graph_kind = input('Do you want to see All data? Scatter graph? Category graph? or Correlation graph? (1,2,3,4) : ')
               while True :
                    if graph_kind == '1':
                         housing.hist(bins=50,figsize=(20,15))
                         plt.title("house_data")
                         plt.show()
                    elif graph_kind == '2':
                         temp_housing = first_housing
                         is_detail = input('Do you want to see detail graph? y/n : ')
                         if is_detail == 'y':
                              plt.scatter(x=temp_housing['longitude'],y=temp_housing['latitude'],alpha=0.4
                                        ,s=temp_housing['population']/100,c=temp_housing['median_house_value'],cmap='jet')
                              plt.colorbar()
                         else:
                              plt.scatter(x=temp_housing['longitude'],y=temp_housing['latitude'],alpha=0.1)
                         print('The graph X is longitude and Y is latitude')
                         plt.title("[Graph before stratified]")
                         plt.show()
                         temp_housing = housing
                         if is_detail == 'y':
                              plt.scatter(x=temp_housing['longitude'],y=temp_housing['latitude'],alpha=0.4
                                        ,s=temp_housing['population']/100,c=temp_housing['median_house_value'],cmap=plt.get_cmap('jet'))
                              plt.colorbar()
                         else:
                              plt.scatter(x=temp_housing['longitude'],y=temp_housing['latitude'],alpha=0.1)
                         plt.title("[Graph after stratified]")
                         plt.show()
                         break
                    elif graph_kind == '3':
                         category_input = input('Please input data category. : ')
                         is_success = is_contain_value(category_value=category_input)
                         if is_success:
                              housing[category_input].hist()
                              plt.title("category_input")
                              plt.show()
                              break
                         elif is_success == False:
                              print('It is not housing configuration')
                    elif graph_kind == '4':
                         while True:
                              _x = input('Please input X : ')
                              _y = input('Please input Y : ')
                              if is_contain_value(category_value=_x) or is_contain_value(category_value=_y):
                                   plt.scatter(x=housing[_x],y=housing[_y],alpha=0.1)
                                   plt.show()
                                   break
                              else:
                                   print('it is not right value')
                    else:
                         print('It is not right.')
                    break
          elif input_value == 'stratified':
               if is_refresh_data == 'y':
                    try:
                         array_sample = sampling_strat(new_value_name=new_category_name)
                         strat_train_set = array_sample[0]
                         strat_test_set = array_sample[1]
                         print('Using stratified train set') 
                         housing = strat_train_set.copy()
                    except:
                         print("This function is unable.")
          elif input_value == 'correlation':
               corr_matrix = housing.corr()
               while True:
                    user_corr = input("Please input correlation : ")
                    if is_contain_value(category_value=user_corr):
                         print(corr_matrix[user_corr].sort_values(ascending=False))
                         attribute = list(housing)
                         scatter_matrix(housing[attribute],figsize=(12,8))
                         plt.rc('axes',labelsize=0.3)
                         plt.show()
                         break
                    else:
                         print('it is not right value')
                    if user_corr == 'exit':
                         break
          
          elif input_value == 'refresh':
               if is_refresh_data == 'y':
                    dividing(new_value_name=new_category_name,housing_ctg_name=housing_category_name)
               print('Complete refresh')

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
                    print('Creat complete')
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