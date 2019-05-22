import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def leaves_by_colors(string):
    red = get_number_of_color(string, 110, 134)
    yellow = get_number_of_color(string, 85, 109) + get_number_of_color(string, 135, 150)
    green = get_number_of_color(string, 0, 84)
    return (red, yellow, green)

def get_number_of_color(string, endpoint1, endpoint2):
    color_count = 0
    for x in range(endpoint1, endpoint2+1):
        color_count = color_count + string.count('Leaf(' + str(x) + ')')
        print('Leaf(' + str(x) + ')')
        print(string.count('Leaf(' + str(x) + ')'))
    return color_count

data = np.loadtxt('test.txt', dtype=str)

without_dead_leaves = data
for x in range (176, 350):
    without_dead_leaves = [string.replace('Leaf(' + str(x) + ')', '') for string in without_dead_leaves]

number_of_leaves = [string.count('Leaf') for string in without_dead_leaves]
iterations = [x for x in range (1, 351)]

print(number_of_leaves)
print(iterations)

fig = plt.figure(1)
ax = fig.add_subplot(111)
ind = np.arange(3)
bars = ax.bar(ind, leaves_by_colors(data[0]), align='center')
bars[0].set_color('red')
bars[1].set_color('yellow')
bars[2].set_color('green')    
ax.set_xticks(ind, ('red', 'yellow', 'green'))
ax.set_ylim(0, 200)

for string in data[1:250]:
    colors = leaves_by_colors(string)
    bars[0].set_height(colors[0])
    bars[1].set_height(colors[1])
    bars[2].set_height(colors[2])
    fig.canvas.draw()
    plt.pause(0.05)

plt.pause(2)

fig1 = plt.figure(2)
ax1 = fig1.add_subplot(111)
ax1.plot(iterations, number_of_leaves[:-250], linestyle='dashed', color='green')

plt.show()