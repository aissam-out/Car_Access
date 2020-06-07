import csv
import rstr
import numpy as np
import pandas as pd
from datetime import datetime

# subject -> role
def empower(org, s):
    # result is a list
    df = pd.read_csv('csv_empower.csv')
    if s in df.cin.values:
      role = df.loc[df['cin'] == s]['role'].item()
    else:
      role = None

    return [org, s, role]

# object -> view
def use(org, o):
    # result is a list
    df = pd.read_csv('csv_use.csv')
    if o in df.plate.values:
      view = df.loc[df['plate'] == o]['view'].item()
    else:
      view = None

    return [org, o, view]

# action -> activity
def consider(org, a):
    # result is a list
    if (a == 1):
        result = [org, a, "a1"]
    elif (a > 1) and (a <= 3):
        result = [org, a, "a2"]
    else:
        result = [org, a, "a3"]

    return result

# start_date & end_date -> context
def check_context(start_d, end_d):
    # result is a list
    # format string to date
    formatted_start = datetime.strptime(start_d, "%Y-%m-%d")
    formatted_end = datetime.strptime(end_d, "%Y-%m-%d")

    # peak season
    summer_s = datetime.strptime('06-01', "%m-%d")
    summer_e = datetime.strptime('08-31', "%m-%d")

    if (formatted_start.month >= summer_s.month) and (formatted_start.month <= summer_e.month):
        result = [start_d, end_d, "peak"]
    elif (formatted_end.month >= summer_s.month) and (formatted_end.month <= summer_e.month):
        result = [start_d, end_d, "peak"]
    else:
        result = [start_d, end_d, "off"]

    return result

# search for the abstract entities in PAP dataset
def check_decision(org, role, view, activity, context):
    # get the decision from the pap
    # get the csv file containing the AC policy
    pap_db = pd.read_csv('csv_pap.csv')
    # processs the request

    df = pap_db.loc[(pap_db['org'] == org) &
                    (pap_db['role'] == role) &
                    (pap_db['view'] == view) &
                    (pap_db['activity'] == activity) &
                    (pap_db['context'] == context)
                    ]

    if df.empty:
        return 'PAP can not process this request'
    elif df.shape[0] > 1:
        return 'multiple matches in the PAP !'
    else:
        return [org, role, view, activity, context, df.proba.item(), df.decision.item()]
