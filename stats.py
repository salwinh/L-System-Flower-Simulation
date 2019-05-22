import numpy as np
import matplotlib.pyplot as plt


def leaves_color_distribution(data):
    fig = plt.figure(1)
    ax = fig.add_subplot(111)
    ind = np.arange(3)

    bars = ax.bar(ind, leaves_by_colors(data[0]), align='center')
    bars[0].set_color('red')
    bars[1].set_color('yellow')
    bars[2].set_color('green')  

    ax.set_title('Leaves color distribution')
    ax.set_xlabel('colors')
    ax.set_ylabel('amount')
    ax.set_xticks(ind, ('red', 'yellow', 'green'))
    ax.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
    ax.set_ylim(0, 1000)
    ax.xaxis.grid(True)
    ax.yaxis.grid(True)

    update_leaves_color_distribution(data, bars, fig)


def update_leaves_color_distribution(data, bars, fig):
    for string in data[1:330]:
        colors = leaves_by_colors(string)
        bars[0].set_height(colors[0])
        bars[1].set_height(colors[1])
        bars[2].set_height(colors[2])
        fig.canvas.draw()
        plt.pause(0.005)

def leaves_over_time(data):
    without_dead_leaves = data
    for x in range (176, 350):
        without_dead_leaves = [string.replace('Leaf(' + str(x) + ')', '') for string in without_dead_leaves]
    number_of_leaves = [string.count('Leaf') for string in without_dead_leaves]

    red = []
    yellow = []
    green = []
    for string in data[:-250]:
        colors = leaves_by_colors(string)
        red.append(colors[0])
        yellow.append(colors[1])
        green.append(colors[2])

    iterations = [x for x in range (1, 351)]

    fig = plt.figure(2)
    ax = fig.add_subplot(111)
    ax.set_title('Leaves amount over time')
    ax.set_xlabel('time')
    ax.set_ylabel('amount')
    ax.plot(iterations, number_of_leaves[:-250], linestyle='dashed', color='black', label='all leaves')
    ax.plot(iterations, red, linestyle='dashed', color='red', label='red leaves')
    ax.plot(iterations, yellow, linestyle='dashed', color='yellow', label='yellow leaves')
    ax.plot(iterations, green, linestyle='dashed', color='green', label='green leaves')
    ax.legend(loc='upper left')

def leaves_by_colors(string):
    red = get_number_of_color(string, 110, 134)
    yellow = get_number_of_color(string, 85, 109) + get_number_of_color(string, 135, 150)
    green = get_number_of_color(string, 0, 84)
    return (red, yellow, green)


def get_number_of_color(string, endpoint1, endpoint2):
    color_count = 0
    for x in range(endpoint1, endpoint2+1):
        color_count = color_count + string.count('Leaf(' + str(x) + ')')
    return color_count


data = np.loadtxt('data.txt', dtype=str)

#leaves_color_distribution(data)
leaves_over_time(data)

plt.show()
