import pandas as pd
from sqlalchemy import create_engine
import numpy as np

# df = pd.read_csv('customer.csv', sep=';')
dfo = pd.read_csv('orders.csv', sep=',')


def to_bool(x):
    """Корректно конвертирует грязные строковые данные в True/False/None"""
    if pd.isna(x):
        return None
    
    x = str(x).strip().lower()

    if x in ("y", "yes", "true", "t", "1"):
        return True
    if x in ("n", "no", "false", "f", "0"):
        return False
    
    return None

dfo['online_order'] = dfo['online_order'].apply(to_bool)
# df['owns_car'] = df['owns_car'].apply(to_bool)

print(dfo.head())

dfo.to_csv('orders_new.csv', sep=',', index=False)