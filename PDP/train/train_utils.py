# import libraries
import random
import itertools
import numpy as np
import pandas as pd
from sklearn.utils import shuffle
import rstr
from catboost import CatBoostRegressor

"""# Training phase

## functions
"""

def gen_pap_db():
  # set the values of abstract entities
  org_values = ['caraccess', 'police', 'partner', 'others']
  role_values = ['normal', 'blacklisted', 'vip']
  view_values = ['normal', 'luxe']
  ay_values = ['a1', 'a2', 'a3']
  ctx_values = ['peak', 'off']

  # generate combinations
  a = [org_values, role_values, view_values, ay_values, ctx_values]
  pap = pd.DataFrame(list(itertools.product(*a)), columns=['org', 'role', 'view', 'activity', 'context'])

  # add proba column
  proba = []
  for i in range(0, 144):
      x = round(random.uniform(0, 1), 2)
      proba.append(x)
  pap['proba'] = proba

  return pap

def gen_ext_db():
  ''' extend db to make roughly 1000 samples'''
  # set the values of abstract entities
  org_values = ['org1', 'org2', 'org3', 'org4', 'org5']
  role_values = ['r1', 'r2', 'r3', 'r4', 'r5']
  view_values = ['v1', 'v2', 'v3', 'v4']
  ay_values = ['a4', 'a5', 'a6']
  ctx_values = ['c1', 'c2', 'c3']

  # generate combinations
  a = [org_values, role_values, view_values, ay_values, ctx_values]
  x_pap = pd.DataFrame(list(itertools.product(*a)), columns=['org', 'role', 'view', 'activity', 'context'])

  # add proba column
  proba = []
  for i in range(0, 900):
      x = round(random.uniform(0, 1), 2)
      proba.append(x)
  x_pap['proba'] = proba

  return x_pap

def gen_ext_2_db():
  ''' extend db to make roughly 10000 samples'''
  # set the values of abstract entities
  org_values = ['org1', 'org2', 'org3', 'org4', 'org5', 'org6', 'org7']
  role_values = ['r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9', 'r10']
  view_values = ['v1', 'v2', 'v3', 'v4', 'v5', 'v6']
  ay_values = ['a4', 'a5', 'a6', 'a7', 'a8']
  ctx_values = ['c1', 'c2', 'c3', 'c4', 'c5']

  # generate combinations
  a = [org_values, role_values, view_values, ay_values, ctx_values]
  xx_pap = pd.DataFrame(list(itertools.product(*a)), columns=['org', 'role', 'view', 'activity', 'context'])

  # add proba column
  proba = []
  for i in range(0, 10500):
      x = round(random.uniform(0, 1), 2)
      proba.append(x)
  xx_pap['proba'] = proba

  return xx_pap

def gen_test_db():
  # set the values of abstract entities
  org_values = ['caraccess', 'police', 'partner', 'others']
  role_values = ['normal', 'blacklisted', 'vip']
  view_values = ['v4', 'v5']
  ay_values = ['a7', 'a8']
  ctx_values = ['peak', 'c4']

  # generate combinations
  a = [org_values, role_values, view_values, ay_values, ctx_values]
  t_pap = pd.DataFrame(list(itertools.product(*a)), columns=['org', 'role', 'view', 'activity', 'context'])

  return t_pap

def gen_extended(df, data_size = 1):
  # real pap data
  real_pap = df
  # create fake pap data
  if (data_size == 1):
      fake_pap = gen_ext_db()
  else :
      fake_pap = gen_ext_2_db()
  # create test data
  test_pap = gen_test_db()
  # concatenate real and fake pap data
  final = pd.concat([real_pap, fake_pap, test_pap], axis=0, ignore_index = True)
  # shuffle the dataset
  #final = shuffle(final)

  return final

def cat_test(db_test, db, index, catreg):
  # predict db_test using CatBoostRegressor catreg
  # index is the index where test dataset begins .. db is the whole dataset
  result = []
  for i in range(index, db.shape[0]):
    test = db_test.loc[i]
    test = pd.DataFrame(test).T
    pred = round(catreg.predict(test).item(), 2)
    result.append(round(pred, 2))

  db_output = db[index:]
  db_output['proba'] = result

  return db_output

def aggreg_df(db, index):
  # this function aggregates the training and the prediction (for a test dataset)
  y = db['proba'][:index]
  X = db.drop('proba',axis=1)
  X = pd.get_dummies(X)

  # split train and test sets
  X_train = X[:index]
  X_test = X[index:]

  # catboost
  catreg = CatBoostRegressor(iterations=1000, depth=6)
  catreg.fit(X_train, y, verbose=0)

  df_pred = cat_test(X_test, db, index, catreg)

  return df_pred

def aggreg_one(db, index):
  # this function aggregates the training and the prediction (for one entry)
  y = db['proba']
  X = db.drop('proba',axis=1)
  X = pd.get_dummies(db)

  # for test
  Xx = X.drop(index)
  yy = y.drop(labels=[index])

  # catboost
  catreg = CatBoostRegressor(iterations=1000, depth=6)
  catreg.fit(Xx, yy, verbose=0)

  t = X.loc[index]
  t = pd.DataFrame(t).T
  pred = round(catreg.predict(t).item(), 2)

  return pred
