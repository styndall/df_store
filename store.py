import numpy as np
import pandas as pd

def store_df(df, filename):
    """
    Store a dataframe as a numpy record array, preserving datatypes
    """
    recs = df.to_records(index=False)
    recstr = repr(recs)
    with open(filename, 'w') as f:
        f.write(recstr)

def get_df(filename):
    """
    Retrieve a dataframe from a stored numpy record array, preserving datatypes
    """
    with open(filename) as f:
        df_str = f.read()
    df_str = "np." + df_str
    df = pd.DataFrame.from_records(eval(df_str))
    return df
    
