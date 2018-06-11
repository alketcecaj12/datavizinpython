import numpy as np
import matplotlib.pyplot as plt
#
pop = [100, 200, 300, 400, 600, 700, 800, 900, 1000, 2000]
# Store pop as a numpy array: np_pop
np_pop = np.array(pop)

gdp_cap = [1000, 2000, 3000, 4000, 6000, 7000, 8000, 9000, 10000, 20000]
life_exp = [50, 60, 65, 45, 70, 73, 75, 80, 83, 85]
# Double np_pop
np_pop = np_pop * 2

# Update: set s argument to np_pop
plt.scatter(gdp_cap, life_exp, s = np_pop)

# Previous customizations
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])

# Display the plot
plt.show()