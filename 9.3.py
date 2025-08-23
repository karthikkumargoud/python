import pandas as pd
import numpy as np

list_data = [10, 20, 30, 40]
series_from_list = pd.Series(list_data)
print("Series from list:")
print(series_from_list)

array_data = np.array([100, 200, 300, 400])
series_from_array = pd.Series(array_data)
print("\nSeries from NumPy array:")
print(series_from_array)

dict_data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
series_from_dict = pd.Series(dict_data)
print("\nSeries from dictionary:")
print(series_from_dict)