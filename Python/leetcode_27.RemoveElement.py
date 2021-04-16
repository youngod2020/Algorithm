# 27. Remove Element
# import pandas as pd
# import numpy as np

# def removeElement(nums, val) -> int:
#     tmp = pd.DataFrame(nums, columns = ['num'])
#     # print(tmp)
#     k = np.sort(tmp[tmp.num.isin([val])==False]['num']).tolist()
#     return len(k)

