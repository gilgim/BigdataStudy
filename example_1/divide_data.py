from posixpath import split
from types import new_class
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit

#    저장안하면 import 되지 않으니 저장 꼭 해야함
from open_data import housing

def dividing(new_value_name,housing_ctg_name):
     housing[new_value_name] = pd.cut(housing[housing_ctg_name]
                              ,bins=[0.,1.5,3.0,4.5,6.,np.inf]
                              ,labels=[1,2,3,4,5])

def sampling_strat(new_value_name):
     splitTemp = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
     for train_index, test_index in splitTemp.split(housing, housing[new_value_name]):
          strat_train_set = housing.loc[train_index]
          strat_test_set = housing.loc[test_index]
     print(strat_test_set[new_value_name].value_counts()/len(strat_test_set))
     #올바른 값을 추출하기 위한 income_cat은 각 훈련셋과 테스트셋에서 지워준다.
     for set_ in (strat_train_set, strat_test_set):
          set_.drop(new_value_name, axis=1, inplace=True)
     # housing.drop(new_value_name,axis=1)
     del housing[new_value_name]
     is_remove = False
     for i in list(strat_train_set):
          if i != new_value_name:
               is_remove = True
     if is_remove:
          print('Removing about "%s"' % new_value_name)
     return [strat_train_set,strat_test_set]

def creat_category(value:str,first:str,second:str):
     housing[value] = housing[first] / housing[second]