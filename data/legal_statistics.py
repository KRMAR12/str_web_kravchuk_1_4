import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
dfrm_legal = pd.read_csv(os.path.join(BASE_DIR, 'dfrm_legal.csv'))
dfrm_predicted = pd.read_csv(os.path.join(BASE_DIR, 'dfrm_predicted.csv'))