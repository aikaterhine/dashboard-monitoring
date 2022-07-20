"""Prepare data for Plotly Dash."""
import pandas as pd
import redis
import json

def create_dataframe():
    """Create Pandas DataFrame from Redis."""
    r = redis.Redis(host='192.168.121.189', port='6379')
    values = r.get('arthurmelo-proj3-output') # MUDAR AQUI PARA catarinapereira-proj3-output
    values = json.loads(values)

    keys_60s = []
    keys_60m = []

    values_60s = []
    values_60m = []

    for i in range(16):
        key_cpu_percent_60sec = 'cpu-percent-60s-' + str(i)
        keys_60s.append(key_cpu_percent_60sec)
        values_60s.append(values.get(key_cpu_percent_60sec))

        key_cpu_percent_60min = 'cpu-percent-60s-' + str(i) # MUDAR AQUI PARA 'cpu-percent-60m-'
        keys_60m.append(key_cpu_percent_60min)
        values_60m.append(values.get(key_cpu_percent_60min))

    df = pd.DataFrame({
        "Metrics_60s": keys_60s,
        "Average_60s": values_60s,
        "Metrics_60m": keys_60m,
        "Average_60m": values_60m
    })
    return df