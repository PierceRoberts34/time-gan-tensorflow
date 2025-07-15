import numpy as np

def time_series_to_sequences(time_series, timesteps):
    '''
    Reshape the time series as overlapping sequences.
    '''
    last_index = len(time_series) - (len(time_series) % timesteps)
    sequences = np.array([
        time_series[t - timesteps: t] 
        for t in range(timesteps, last_index + 1, timesteps)
    ])
    return sequences


def sequences_to_time_series(sequences):
    '''
    Reshape the sequences as time series.
    '''
    time_series = np.concatenate([sequence for sequence in sequences], axis=0)
    return time_series

