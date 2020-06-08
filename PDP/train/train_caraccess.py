"""train_caraccess.ipynb
Google Colaboratory file is located at https://colab.research.google.com/drive/1xt1o0dj2BAoFZXR7ZrTq0mA71DV1yF-f
"""

# import modules
import itertools
from train_utils import *

"""## Prepare data"""
def main_func(data_size = 1):
    db = gen_pap_db()
    # manual labels of the generated list
    access_list = [0.9, 1.0, 0.8, 0.9, 0.75, 0.8,
                  0.8, 0.8, 0.8, 0.8, 0.72, 0.75,
                  0.4, 0.45, 0.39, 0.4, 0.3, 0.35,
                  0.2, 0.2, 0.2, 0.2, 0.2, 0.2,
                  1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                  0.95, 1.0, 0.95, 1.0, 0.9, 1.0]
    police_list = [0.9, 1.0, 0.9, 0.9, 0.9, 0.9,
                  0.85, 0.85, 0.85, 0.85, 0.85, 0.85,
                  0.4, 0.45, 0.39, 0.4, 0.3, 0.35,
                  0.2, 0.2, 0.2, 0.2, 0.2, 0.2,
                  1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                  0.95, 1.0, 0.95, 1.0, 0.9, 1.0]
    partner_list = [0.9, 1.0, 0.8, 0.9, 0.8, 0.8,
                  0.8, 0.8, 0.8, 0.8, 0.8, 0.8,
                  0.4, 0.45, 0.39, 0.4, 0.3, 0.35,
                  0.2, 0.2, 0.2, 0.2, 0.2, 0.2,
                  1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                  0.97, 1.0, 0.97, 1.0, 0.95, 1.0]
    others_list = [0.89, 0.9, 0.78, 0.89, 0.78, 0.78,
                  0.78, 0.78, 0.78, 0.78, 0.78, 0.78,
                  0.34, 0.4, 0.35, 0.34, 0.23, 0.3,
                  0.12, 0.12, 0.12, 0.12, 0.12, 0.12,
                  0.9, 0.9, 0.9, 0.9, 0.9, 0.9,
                  0.9, 0.9, 0.9, 0.9, 0.9, 0.9]
    list_proba = list(itertools.chain(access_list, police_list, partner_list, others_list))

    # this is the real data with labels
    db['proba'] = list_proba

    if (data_size == 1):
        # add test and fake data
        xdb = gen_extended(db, 1)

        """## aggregated training"""
        # 144 real, 900 fake = 1044(index) ; then 96 test = 1140
        # OR
        # 144 real, 10500 fake = 10644(index) ; then 96 test = 10740
        index = 1044
    else :
        xdb = gen_extended(db, 2)
        index = 10644

    df_pred = aggreg_df(xdb, index)

    return df_pred

df_pred = main_func(data_size = 1)

csv_pred = df_pred.to_csv('csv_predictions.csv', index = False)


# test just one entry (via index)
#aggreg_one(xdb, 117)
