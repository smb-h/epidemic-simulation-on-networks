import random
import time
import pandas as pd




# lane length
lanes = 10000

Start = time.time()

data_list = []
for i in range(lanes):
    x = random.randint(0, 10000)
    y = random.randint(0, 10000)
    data_list.append([x, y, 0])


data = pd.DataFrame(data_list)
data.to_excel('ExcelData.csv')

print('Time : ', time.time() - Start)
