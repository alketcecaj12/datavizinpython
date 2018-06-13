import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#sns.residplot(x='age',y='fare',data=tips,color='indianred')
# Generate a green residual plot of the regression between 'hp' and 'mpg'

auto = pd.read_csv('auto.csv')

print(auto)
sns.residplot(x='hp', y='mpg', data=auto, color='green')

# Display the plot
plt.show()