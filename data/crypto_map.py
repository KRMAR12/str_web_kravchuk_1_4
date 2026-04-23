import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
status_by_country = pd.read_csv(os.path.join(BASE_DIR, 'status_by_country.csv'))