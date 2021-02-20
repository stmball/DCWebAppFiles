import pandas as pd
import numpy as np

def convert(dataset):
    data = pd.read_csv(dataset)
    newdata = data[["Time", "Noisy Current"]].to_numpy()
    np.savetxt(dataset, newdata, fmt='%f', delimiter=",")
    return 1

print(convert("./Datasets/ten_channel_simulated"))