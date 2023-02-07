########## MATPLOTLIB 

# Print the last item from year and pop
print(year[-1]) 
print(pop[-1])
# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
# Make a line plot: year on the x-axis, pop on the y-axis
plt.plot(year, pop)
# Display the plot with plt.show()
plt.show()



# Print the last item of gdp_cap and life_exp
print(gdp_cap[-1], life_exp[-1])
# Make a line plot, gdp_cap on the x-axis, life_exp on the y-axis
#import matplotlib.pyplot as plt
plt.plot(gdp_cap, life_exp)
# Display the plot
plt.show()

# Print the last item of gdp_cap and life_exp
print(gdp_cap[-1])
print(life_exp[-1])
# Make a line plot, gdp_cap on the x-axis, life_exp on the y-axis
plt.plot(gdp_cap, life_exp)
# Display the plot
plt.show()


# Change the line plot below to a scatter plot
#plt.plot(gdp_cap, life_exp)
plt.scatter(gdp_cap, life_exp)
# Put the x-axis on a logarithmic scale
plt.xscal
# Show plot
plt.show()

########## Histogram 
help(plt.hist)
    #most impt parameters are bins and data set
plt.hist(values, bins=3)

# LABELS
plt.scatter(gdp_cap, life_exp)  ;  plt.xscale('log') 
# Define axis labels, add to plot
xlab = 'GDP per Capita [in USD]'
ylab = 'Life Expectancy [in years]'
plt.xlabel(xlab)
plt.ylabel(ylab)
### define the title and add it to plot
title = 'World Development in 2007'
plt.title(title)
plt.show()


######## TICKS

# Scatter plot
plt.scatter(gdp_cap, life_exp)
# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
# Definition of tick_val and tick_lab
tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']
# Adapt the ticks on the x-axis
plt.xticks(tick_val, tick_lab)
# After customizing, display the plot
plt.show()


########## Dictionaries
# curly braces {} and colons : to select keys and values
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# add a key value pair
europe["italy"] = "rome"
#check that italy is in europe
print("italy" in europe)

# delete a key value pair
del(europe["spain"])
#check that spain is not in europe
print("spain" in europe)

# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 }
        }
# print out the capital of France
print(europe["france"]["capital"])

# Create sub-dictionary data
data = { "capital":"rome", "population":59.83 }

# Add data to europe under key 'italy'
europe["italy"] = data

# Print europe
print(europe)
