import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#sns.residplot(x='age',y='fare',data=tips,color='indianred')
# Generate a green residual plot of the regression between 'hp' and 'mpg'

auto = pd.read_csv('auto.csv')

# Make a strip plot of 'hp' grouped by 'cyl'
plt.subplot(2,1,1)
sns.stripplot(x='cyl', y='hp', data=auto)

# Make the strip plot again using jitter and a smaller point size
plt.subplot(2,1,2)
sns.stripplot(x = 'cyl', y = 'hp', data = auto, jitter = True, size = 3)

# Display the plot
plt.show()