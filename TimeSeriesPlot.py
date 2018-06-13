from pandas import Series
import matplotlib.pyplot as plt

from pandas import read_csv
series = read_csv('daily-total-female-births-in-cal.csv', header=0, parse_dates=[0], index_col=0, squeeze=True)
print(type(series))
print(series.head())

plt.plot(series)
plt.show()