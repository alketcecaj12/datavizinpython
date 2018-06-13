import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#sns.residplot(x='age',y='fare',data=tips,color='indianred')
# Generate a green residual plot of the regression between 'hp' and 'mpg'

auto = pd.read_csv('auto.csv')

# Plot a linear regression between 'weight' and 'hp', with a hue of 'origin' and palette of 'Set1'
sns.lmplot(x='weight', y='hp', data=auto, hue='origin', palette='Set1')

# Display the plot
plt.show()