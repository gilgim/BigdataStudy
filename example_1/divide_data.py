from posixpath import split
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
     split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
     for train_index, test_index in split.split(housing, housing[new_value_name]):
          strat_train_set = housing.loc[train_index]
          strat_test_set = housing.loc[test_index]
     print(strat_test_set[new_value_name].value_counts()/len(strat_test_set))
     #올바른 값을 추출하기 위한 income_cat은 각 훈련셋과 테스트셋에서 지워준다.
     print('Removing %s' % new_value_name)
