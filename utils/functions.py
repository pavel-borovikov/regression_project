
import numpy as np
import pandas as pd

def select_timeframe(df, start_date, end_date, event=None, delay=0):
    """Select data from a window of dates.

    Attributes : 
    ------------

    df: pandas.DataFrame object
        Must contain a date column as numpy.datetime64 objects

    start_date: str
        string of the selected start date in YYYY-MM-DD

    end_date: str
        string of the selected end date in YYY-MM-DD

    event: str
        string of the event date in YYY-MM-DD


    
    Output :
    ------------

    Returns a pandas.DataFrame object.

    If event argument is passed, the output DataFrame will include time before and after the event in days.

    Regardless if the event argument is passed, the output DataFrame will contain a days_from_start column.

    """

    start, end = np.datetime64(start_date), np.datetime64(end_date)
    mask = (df['date'] >= start) & (df['date'] <= end)
    
    df = df.loc[mask].sort_values('date')
    
    if event == None:
        days_delta = 0
        
    else:
        days_delta = (start - np.datetime64(event)).astype(int)
        df['days_from_event'] = range(0 + days_delta, len(df)+ days_delta)
        df['after'] = np.where(df['days_from_event'] > delay, 1, 0)
    
    
    df['days_from_start'] = range(len(df))

    return df