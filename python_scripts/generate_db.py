import csv
import rstr
import numpy as np
import pandas as pd

def gen_emp_db(num):
  # generate org
  org_values = ['caraccess', 'police', 'partner', 'others']
  org = np.random.choice(org_values, num, p=[0.2, 0.1, 0.3, 0.4])

  # generate cin
  cin = [None] * num
  for i in range(num):
    cin[i] = rstr.xeger(r'[A-Z][A-Z]\d\d\d\d')

  # generate badge
  badge = np.random.choice(2, num, p=[0.7, 0.3])

  # generate role
  role_values = ['normal', 'blacklisted']
  role = np.random.choice(role_values, num, p=[0.7, 0.3])

  # df aggregation
  empower = {'org':  org,
            'cin': cin,
            'badge': badge,
            'role': role
            }
  df_empower = pd.DataFrame(empower, columns = ['org', 'cin', 'badge', 'role'])

  # solve conflict between badge and vip
  for i in range(num):
    if df_empower.badge[i] == 1:
      df_empower.role[i] = "vip"

  df_empower.to_csv('csv_empower.csv', index = False)

  return df_empower

def gen_use_db(num):
  # generate org (whether the car is ours or in possession of a partner)
  org_values = ['caraccess', 'partner']
  org = np.random.choice(org_values, num, p=[1, 0])

  # generate plate
  plate = [None] * num
  for i in range(num):
    plate[i] = rstr.xeger(r'[A-Z][A-Z] \d\d\d\d')

  # generate company
  company_values = ['mercedes', 'porsche', 'renault', 'audi', 'lamborghini', 'ferrari', 'hyundai', 'tesla']
  company = np.random.choice(company_values, num)

  # df aggregation
  mod = [None] * num
  use = {'org':  org,
         'plate': plate,
         'company': company,
         'model':mod
         }
  df_use = pd.DataFrame(use, columns = ['org', 'plate', 'company', 'mod'])

  # generate model
  for i in range(num):
    if (df_use.company[i]=='mercedes'):
      df_use.at[i,'mod'] = np.random.choice(['GLA SUV,normal', 'Mercedes-Maybach,luxe'], p=[0.6, 0.4])
    if (df_use.company[i]=='porsche'):
      df_use.at[i,'mod'] = np.random.choice(['911 Turbo S Cabriolet,luxe', '718 Cayman GT4,luxe'], p=[0.6, 0.4])
    if (df_use.company[i]=='renault'):
      df_use.at[i,'mod'] = np.random.choice(['Megane Sedan,normal', 'Fluence SEDANS,normal'], p=[0.6, 0.4])
    if (df_use.company[i]=='audi'):
      df_use.at[i,'mod'] = np.random.choice(['Q3,normal', 'SQ8,luxe'], p=[0.6, 0.4])
    if (df_use.company[i]=='lamborghini'):
      df_use.at[i,'mod'] = np.random.choice(['Huracán Evo,luxe', 'Aventador S,luxe'], p=[0.6, 0.4])
    if (df_use.company[i]=='ferrari'):
      df_use.at[i,'mod'] = np.random.choice(['F8 Tributo,luxe', '488 Pista Spider,luxe'], p=[0.6, 0.4])
    if (df_use.company[i]=='hyundai'):
      df_use.at[i,'mod'] = np.random.choice(['Accent,normal', 'Tucson,normal'], p=[0.6, 0.4])
    if (df_use.company[i]=='tesla'):
      df_use.at[i,'mod'] = np.random.choice(['model 3,normal', 'Roadster,luxe'], p=[0.6, 0.4])

  # split model and view colums
  df_use[['model','view']] = df_use['mod'].str.split(",",expand=True,)
  df_use.drop('mod', axis=1, inplace=True)

  csv_use = df_use.to_csv('csv_use.csv', index = False)
  with open(r'use.csv', 'a') as f:
      writer = csv.writer(f)
      writer.writerow(csv_use)

  return df_use
