import matplotlib.pyplot as plt

# load data
pop = [100, 200, 300, 500]




# data for hist
life_exp2 = [60,60,60, 70,70, 80, 80,80, 80, 80,90,90,90,100,100]

# data
gdp_cap = [2000, 3000, 5000, 12000, 25000,18000, 19000, 20000]
life_exp = [60, 70, 80, 90, 90, 90, 95, 97]

#scatterplot
plt.scatter(gdp_cap, life_exp)
plt.xscale('log')

# Strings
xlab = 'GDP per Capita [in USD]'
ylab = 'Life Expectancy [in years]'
title = 'World Development in 2007'

# Add axis labels

plt.xlabel(xlab)
plt.ylabel(ylab)
# Add title
plt.title(title)

# After customizing, display the plot
plt.show()