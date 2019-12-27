import random
import time
import pandas as pd




# lane length
lanes = 1500

Start = time.time()

data_list = []
for i in range(lanes):
    x = random.randint(0, 100000)
    y = random.randint(0, 100000)
    data_list.append([x, y, 0, "b"])


# infect 1
infect_indx =random.randint(0, lanes)
data_list[infect_indx][3] = "r"


data = pd.DataFrame(data_list)
data.to_csv('data.csv')

print('Time : ', time.time() - Start)
