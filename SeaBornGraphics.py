# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

auto = pd.read_csv('auto.csv')

print(auto)
# Plot a linear regression between 'weight' and 'hp'
sns.lmplot(x='weight', y='hp', data=auto)
print(auto)
# Display the plot
plt.show()