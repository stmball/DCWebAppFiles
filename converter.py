import pandas as pd
import numpy as np

def convert(dataset):
    data = pd.read_csv(dataset)
    newdata = data[["Time", "Noisy Current"]][:100000].to_numpy()
    np.savetxt(f'{dataset}_new', newdata, fmt='%f', delimiter=",")
    return 1

print(convert("./Datasets/single_channel.csv"))
