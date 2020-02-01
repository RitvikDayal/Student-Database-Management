import pandas as pd
from pandas import DataFrame

def store_data(n, ad, p, eml, des, imge):  
    df = pd.read_csv('Client Data.csv')
    temp_df = pd.DataFrame({'Name': [n],'Address' : [ad],'Phone' : [p], 'Email' : [eml],'Client Description' : [des],'Image' : [imge]})
    df.append(temp_df,sort=False)
    df.to_csv('Client Data.csv')
    
    