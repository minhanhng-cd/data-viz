# Data Visualization with Matplotlib - MATLAB Style

import matplotlib.pyplot as plt
import numpy as np

#----User Input----
WIDTH = 0.25
HEIGHT = 3000
#------------------

#----Input Data----
dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

py_dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

#------------------

# Change plot style
plt.style.use("fivethirtyeight")

# Sort the age in decending order
# dev_x.reverse()
# dev_y.reverse()
# py_dev_x.reverse()
# py_dev_y.reverse()

# Creat index for X-axis
x_index = np.arange(len(dev_x))

# Plot Title
plt.title('Mean Salary (USD) of Developers by Age')

# X-axis title
plt.xlabel('Age')

# Y-axis title
plt.ylabel('Mean Salary (USD)')

# Plot data of all developers
plt.bar(x_index - WIDTH, dev_y, width = WIDTH, color = 'navy', label = 'All dev.')

# Plot data of Python developers
plt.bar(x_index, py_dev_y, width = WIDTH, color = 'orange', label = 'Python')

# X-axis ticks
plt.xticks(ticks = x_index - WIDTH / 2, labels = dev_x)

# Data Label
for x, y_dev, y_python in zip(x_index, dev_y, py_dev_y):

    # print(f'{x}, {y_dev}, {y_python}')
    
    plt.text(x = x - WIDTH, y = y_dev - HEIGHT, color = 'white', s =  f'{y_dev:,}', rotation = 'vertical', va = 'top', ha = 'center')

    plt.text(x = x, y = y_python - HEIGHT, color = 'white', s = f'{y_python:,}', rotation = 'vertical', va = 'top', ha = 'center')


# Add legend
plt.legend()

# Make the plot fit better to smaller windows
plt.tight_layout()


# Show the plot
plt.show()