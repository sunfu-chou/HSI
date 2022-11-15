#! python3
import bagpy
from bagpy import bagreader
import pandas as pd
import matplotlib.pyplot as plt

b = bagreader('/home/sunfu/Downloads/HSI/rad_2022-11-14-09-23-32.bag')
csv_file = b.message_by_topic('dji_m210/openhsi/radiance')
df = pd.read_csv(csv_file)

times = 20
space = 150
spe = df.iloc[times, 8 + space * 131 : 8 + (space + 1) * 131]
plt.plot(spe)
# plt.ylim([0, 30])
plt.show()
