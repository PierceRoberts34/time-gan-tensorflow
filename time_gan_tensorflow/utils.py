import numpy as np

def time_series_to_sequences(time_series, timesteps):
    '''
    Reshape the time series as overlapping sequences.
    '''
    sequences = np.array([
        time_series[i: i + timesteps] 
        for i in range(len(time_series) - timesteps + 1)
    ])
    return sequences



def sequences_to_time_series(sequences):
    '''
    Reshape the sequences as time series.
    '''
    time_series = np.concatenate([sequence for sequence in sequences], axis=0)
    return time_series

