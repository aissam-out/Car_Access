'''
Protect the privacy of the collected new features
'''
import numpy as np
import random

# columns = list(X.columns)

def randomized_reponse(truth, treshold, columns):
  # the principle is : tell the truth (treshold*100) percent of the time
  if truth in columns:
    rnd = random.uniform(0, 1)
    if (rnd <= treshold):
      result = truth
    else:
      lst = list(columns)
      lst.remove(truth)
      result =  np.random.choice(lst)
      # in a more robust version, it is important that lst represents the set of all possibilities - {truth}

  else:
    raise Exception("Your true answer must be one of the X columns")

  return result
